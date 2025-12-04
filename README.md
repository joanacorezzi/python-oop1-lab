# Bookstore OOP Lab

This project is a small Object Oriented Programming lab for a bookstore.  
It has two Python classes: `Book` and `Coffee`.

## Book

- Attributes:
  - `title`
  - `page_count`
- Behavior:
  - `page_count` must be an integer, otherwise it prints:  
    `page_count must be an integer`
  - `turn_page()` prints:  
    `Flipping the page...wow, you read fast!`

## Coffee

- Attributes:
  - `size` (Small, Medium, or Large)
  - `price`
- Behavior:
  - `size` must be `Small`, `Medium`, or `Large`, otherwise it prints:  
    `size must be Small, Medium, or Large`
  - `tip()` prints:  
    `This coffee is great, here’s a tip!`  
    and increases `price` by 1.

## Tests

All tests are passing

## How to Run

```bash
pipenv install
pipenv shell
pytest lib/testing
