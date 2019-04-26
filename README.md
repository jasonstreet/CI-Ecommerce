# Project 4 - E-Commerce

Medical e-commerce website built using Django, python, javascript, HTML and CSS

## Table of Contents  
1. [Deployment](#Deployment)  
2. [Testing](#Testing) 
3. [Goals](#Goals)
4. [Improvements](#Improvements)
5. [Credits](#Credits)

## Deployment <a name="Deployment"></a>


## Testing <a name="Testing"></a>

In order to test my application, I used Djangos in-built testing framework. I created seperate test files for different sections of my application, such as the payment form, account creation, and product selection.

```
    def test_no_submit_without_name(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        
    def test_no_submit_without_credit_card(self):
        form = MakePaymentForm({'Credit card number': ''})
        self.assertFalse(form.is_valid())
```
Here I have created tests for the payment form, to check if the form can be submitted under certain conditions, like whether or not the form can be submit without certain fields like name and the credit card information. Having tests for my payment details form was useful when working with the Stripe API, as I was able to test for error before writing my actual error codes for the end user.

## Goals <a name="Goals"></a>

The idea for this website is to make buying/paying for medication easier for people. Right now most people pick up their medicine from a pharmacist or doctor's practice, but I think in the future medication will be bought online by most people, for it's convienience. I think a lot of older people could benefit from such a website. With that in made, I have made the website easy to use, from selecting items, all the way to paying for them. I have include a FAQ modal as well which contains all the details about the website.


## Improvements <a name="Improvements"></a>


## Built With <a name="Credits"></a>

* CSS3
* HTML5
* JavaScript
* Python
* Django

## Authors

* **Jason Street** - *For Code Institute*

## Acknowledgments

* Stripe (For API)
* Google (For images)
