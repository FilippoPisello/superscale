import re

from measurehero import constants as CN


def clean_product_name(product_name: str) -> str:
    return product_name.replace(",", ".").replace("*", "x").rstrip()


def extract_units_info(product_name: str) -> int:
    product_name = clean_product_name(product_name)

    if pieces_words_in_name(product_name):
        res = re.search(r"((?<!\d)x\d+)", product_name)
        if res:
            return int(res.group(0).replace(" ", "").replace("x", ""))
        res = re.search(r"(\s*\d+)", product_name)
        if res:
            return int(res.group(0).replace(" ", ""))

    re_basic_uoms_eos = rf"(\d+\s*x\s*({CN.RE_UNIT_QTY})\s*({CN.RE_ALL_UOMS})$)"
    res = re.search(re_basic_uoms_eos, product_name)
    if res:
        return int(res.group(0).replace(" ", "").split("x")[0])

    re_basic_uoms_eos = rf"(\d+\s?x\s?({CN.RE_UNIT_QTY})\s?({CN.RE_ALL_UOMS}))"
    res = re.search(re_basic_uoms_eos, product_name)
    if res:
        return int(res.group(0).replace(" ", "").split("x")[0])

    res = re.search(r"((?<!\d)x\d+)", product_name)
    if res:
        return int(res.group(0).replace(" ", "").replace("x", ""))

    return 1


def extract_unitary_weight_info(product_name: str) -> float:
    product_name = clean_product_name(product_name)

    re_length = r"\d+ (metres|metre)"
    res = re.search(re_length, product_name)
    if res:
        res = res.group(0)
        return get_number_only(res)

    # try first to get from pieces form
    re_basic_uoms_eos = rf"(\d+\s*x\s*({CN.RE_UNIT_QTY})\s*({CN.RE_ALL_UOMS}))"
    res = re.search(re_basic_uoms_eos, product_name)
    if res:
        return get_number_only(res.group(0).replace(" ", "").split("x")[1])

    re_basic_uoms_eos = rf"(({CN.RE_UNIT_QTY})\s*({CN.RE_ALL_UOMS})$)"
    res = re.search(re_basic_uoms_eos, product_name)
    if res:
        res = res.group(0)
        return get_number_only(res)

    res = re.search(re_basic_uoms_eos.replace("$", ""), product_name)
    if res:
        res = res.group(0)
        return get_number_only(res)

    return None


def extract_uom_info(product_name: str) -> str:
    product_name = clean_product_name(product_name)

    re_basic_uoms_eos = rf"(({CN.RE_UNIT_QTY})\s*({CN.RE_ALL_UOMS})$)"
    res = re.search(re_basic_uoms_eos, product_name)
    if res:
        res = res.group(0)
        return get_uom(res)

    res = re.search(re_basic_uoms_eos.replace("$", ""), product_name)
    if res:
        res = res.group(0)
        return get_uom(res)

    return None


def extract_multiply_info(product_name: str) -> bool:
    product_name = clean_product_name(product_name)

    re_basic_uoms_eos = rf"(\d+\s*x\s*({CN.RE_UNIT_QTY})\s*({CN.RE_ALL_UOMS}))"
    res = re.search(re_basic_uoms_eos, product_name)
    if res:
        return True
    return False


def pieces_words_in_name(product_name: str) -> bool:
    PIECES_WORDS = [
        "sachet",
        "sachets",
        "capsule",
        "capsules",
        "disc",
        "discs",
        "doses",
        "dose",
        "pochettes",
        "pochette",
    ]
    return any([word in product_name for word in PIECES_WORDS])


def get_number_only(number_and_uom: str) -> float:
    return float("".join([c for c in number_and_uom if c.isdigit() or c == "."]))


def get_uom(number_and_uom: str) -> str:
    res = re.search(rf"(({CN.RE_ALL_UOMS}))", number_and_uom)
    return res.group(0)
