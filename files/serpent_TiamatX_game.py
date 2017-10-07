from serpent.game import Game

from .api.api import TiamatXAPI

from serpent.utilities import Singleton




class SerpentTiamatXGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "Tiamat X"

        kwargs["app_id"] = "343340"
        kwargs["app_args"] = None

        super().__init__(**kwargs)

        self.api_class = TiamatXAPI
        self.api_instance = None

        self.frame_transformation_pipeline_string = "RESIZE:100x100|GRAYSCALE"

        self.frame_width = 100
        self.frame_height = 100
        self.frame_channels = 0        

    @property
    def screen_regions(self):
        regions = {
            "HP_AREA": (21, 621, 48, 750),
            "SCORE_AREA": (24, 37, 37, 118)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
