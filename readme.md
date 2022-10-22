# SuperScale: extract measurements from strings
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub license](https://badgen.net/github/license/FilippoPisello/superscale)](https://github.com/FilippoPisello/superscale/blob/main/LICENSE)
## What is it?
SuperScale allows you to parse units, weight and unit of measure from strings. It is built for groceries so it works at its best with names of supermarket
articles.

Under the hood, it is just a wrapper around some ReGex that looks for combinations of digits and unit of measures.

## Quick Start
### Installation
You can install EasyPred via `pip`
```
pip install superscale
```
Alternatively, you can install EasyPred by cloning the project to your local directory
```
git clone https://github.com/FilippoPisello/SuperScale
```
And then run `setup.py`
```
python setup.py install
```

### Usage
With a simple item name:
```python
>>> from superscale import ArticleMeasure
>>> article = "Heinz Baked Beans In Tomato Sauce 4X415g"
>>> measure = ArticleMeasure.from_string("Heinz Baked Beans In Tomato Sauce 4X415g")
>>> measure.units
4
>>> measure.unitary_measure
415.0
>>> measure.total_measure
1660.0
>>> measure.unit_of_measure
'g'
```

## Dependencies
SuperScale has no external dependencies.

## License
[MIT](LICENSE)