# SuperScale: extract measurements from strings
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub license](https://badgen.net/github/license/FilippoPisello/SuperScale)](https://github.com/FilippoPisello/SuperScale/blob/main/license.md)
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
>>> import superscale
>>> superscale.scrape_measures("Heinz Baked Beans In Tomato Sauce 4X415g")
ItemMeasure(units=4, unitary_measure=415.0, total_measure=1660.0,
unit_of_measure='g')
>>> superscale.scrape_measures("Bell peppers x5 extra fresh")
ItemMeasure(units=5, unitary_measure=None, total_measure=None, unit_of_measure=None)
>>> superscale.scrape_measures("Coca-cola zero 1l")
ItemMeasure(units=1, unitary_measure=1.0, total_measure=1.0, unit_of_measure='l')
>>> superscale.scrape_measures("Olive oil 1/2 liter")
ItemMeasure(units=1, unitary_measure=0.5, total_measure=0.5, unit_of_measure='liter')
```
The package also supports simple conversion to standard unit of measures:
```python
>>> import superscale
>>> article = "Heinz Baked Beans In Tomato Sauce 4X415g"
>>> measure = superscale.scrape_measures(article)
>>> measure.convert()
>>> measure
ItemMeasure(units=4, unitary_measure=0.415, total_measure=1.66, unit_of_measure='kilo')
```


## Dependencies
SuperScale has no external dependencies.

## License
[MIT](LICENSE)