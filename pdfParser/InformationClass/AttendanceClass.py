import pdfplumber
import os

table_settings = {
    "vertical_strategy" : "lines_strict",
    "horizontal_strategy" : "lines_strict",
    "keep_blank_chars": True,
    "text_tolerance": 1,
    "text_x_tolerance": 1
}