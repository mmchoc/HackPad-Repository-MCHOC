
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers


from kmk.extensions.RGB import RGB


keyboard = KMKKeyboard()


keyboard.row_pins = ("GP4", "GP2", "GP1")   
keyboard.col_pins = ("GP6", "GP7", "GP0")  
keyboard.diode_orientation = DiodeOrientation.COLUMNS_TO_ROWS


keyboard.modules.append(Layers())


rgb = RGB(
    pixel_pin="GP3",
    num_pixels=2,
)

rgb.val_limit = 140     
rgb.val_default = 163
rgb.hue_default = 75    
rgb.sat_default = 91

keyboard.extensions.append(rgb)


class ReactiveRGB:
    def __init__(self, rgb_ext: RGB):
        self.rgb = rgb_ext
        self.enabled = False
        self.flash_until = 0.0
        self.flash_ms = 120
        self.flash_val = 255
        self.base_h = None
        self.base_s = None
        self.base_v = None

    def remember_base(self):
        self.base_h = getattr(self.rgb, "hue", self.rgb.hue_default)
        self.base_s = getattr(self.rgb, "sat", self.rgb.sat_default)
        self.base_v = getattr(self.rgb, "val", self.rgb.val_default)

    def set_enabled(self, on: bool):
        self.enabled = on
        self.flash_until = 0.0
        if on:
            self.remember_base()
            self.rgb.set_hsv_fill(self.base_h, self.base_s, self.base_v)

    def process_key(self, keyboard, key, is_pressed, int_coord):
        if self.enabled and is_pressed:
            now = time.monotonic()
            self.flash_until = now + (self.flash_ms / 1000.0)
            self.rgb.set_hsv_fill(self.base_h, self.base_s, self.flash_val)
        return key

    def after_matrix_scan(self, keyboard):
        if self.enabled and self.flash_until and time.monotonic() >= self.flash_until:
            self.flash_until = 0.0
            self.rgb.set_hsv_fill(self.base_h, self.base_s, self.base_v)

reactive = ReactiveRGB(rgb)
keyboard.modules.append(reactive)


def _set_breathe(key, keyboard, *args, **kwargs):
    reactive.set_enabled(False)
    keyboard.tap_key(KC.RGB_MODE_BREATHE)

def _set_reactive(key, keyboard, *args, **kwargs):
    reactive.remember_base()
    rgb.set_hsv_fill(reactive.base_h, reactive.base_s, reactive.base_v)
    reactive.set_enabled(True)

def _set_off(key, keyboard, *args, **kwargs):
    reactive.set_enabled(False)
    rgb.off()

make_key(names=("RGB_BREATHE",), on_press=_set_breathe)
make_key(names=("RGB_REACT",), on_press=_set_reactive)
make_key(names=("RGB_OFF",), on_press=_set_off)

HOME_LT1 = KC.LT(1, KC.HOME)

keyboard.keymap = [
    
    [
        KC.ESC,   HOME_LT1, KC.DEL,
        KC.TAB,   KC.UP,    KC.ENTER,
        KC.LEFT,  KC.DOWN,  KC.RIGHT,
    ],
    
    [
        KC.RGB_BREATHE, KC.RGB_REACT, KC.RGB_OFF,
        KC.TRNS,        KC.TRNS,      KC.TRNS,
        KC.TRNS,        KC.TRNS,      KC.TRNS,
    ],
]

if __name__ == "__main__":
    keyboard.go()