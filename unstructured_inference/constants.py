from enum import Enum


class AnnotationResult(Enum):
    IMAGE = "image"
    PLOT = "plot"


class Source(Enum):
    YOLOX = "yolox"
    DETECTRON2_ONNX = "detectron2_onnx"
    DETECTRON2_LP = "detectron2_lp"
    CHIPPER = "chipper"
    CHIPPERV1 = "chipperv1"
    CHIPPERV2 = "chipperv2"
    MERGED = "merged"
    SUPER_GRADIENTS = "super-gradients"


class ElementType:
    IMAGE = "Image"
    FIGURE = "Figure"
    PICTURE = "Picture"
    TABLE = "Table"
    LIST = "List"
    LIST_ITEM = "List-item"
    FORMULA = "Formula"
    CAPTION = "Caption"
    PAGE_HEADER = "Page-header"
    SECTION_HEADER = "Section-header"
    PAGE_FOOTER = "Page-footer"
    FOOTNOTE = "Footnote"
    TITLE = "Title"
    TEXT = "Text"
    UNCATEGORIZED_TEXT = "UncategorizedText"
    PAGE_BREAK = "PageBreak"


FULL_PAGE_REGION_THRESHOLD = 0.99

# this field is defined by pytesseract/unstructured.pytesseract
TESSERACT_TEXT_HEIGHT = "height"
