# Project 4 - E-Commerce

Medical e-commerce website built using Django, python, javascript, HTML and CSS.

## Table of Contents  
1. [Deployment](#Deployment)  
2. [Testing](#Testing) 
3. [Goals](#Goals)
4. [Improvements](#Improvements)
5. [Credits](#Credits)

## Deployment <a name="Deployment"></a> 

The application has been deployed through Heroku. The live website can be accessed at: https://medicine-cabinet-js.herokuapp.com/
Due to unknown reasons the application does not seem to work on Vivaldi browsers. After investigating the issue, I have not been able to find a clear reason as to why the website sometimes fails to load on Vivaldi. This could be a bug within Vivaldi itself, as the website works fine on other Browsers.
![Vivaldi Error](https://i.imgur.com/YT87yK7.png)

For the live version of this website, I have disabled debugging mode in my Django application settings by changing ```DEBUG = True``` to False. This means that the user won't see Django error messages (like the above) if the page fails to load for whatever reason, they will instead see regular HTTP errors, such as 404 not found for example.

To deploy the website, I deployed via the master Github branch through Heroku. To do this, I went into the Deployment section of my Heroku application settings, selected Master branch under manual deployment, and deployed from there. I also added my secret keys and URLs to my Heroku config variables, and then removed the hard coded values from my code. This was done for security purposes.

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

As with any website, I also tested it for responsivness and usability on other devices. My images and text scaled appropriately when re-sized, and the interactive menu also changed to adapt to mobile devices and smaller screens by scaling into an accordian dropdown. This prevents the menu from obscuring any information when displayed on a small screen or mobile device. As mentioned above, the website sometimes fails to load on Vivaldi, however I believe this may be a bug (this has also been discussed with other developers).

## Goals <a name="Goals"></a>

The idea for this website is to make buying/paying for medication easier for people. Right now most people pick up their medicine from a pharmacist or doctor's practice, but I think in the future medication will be bought online by most people, for it's convienience. I think a lot of older people could benefit from such a website. With that in made, I have made the website easy to use, from selecting items, all the way to paying for them. I have include a FAQ modal as well which contains all the details about the website.


## Improvements <a name="Improvements"></a>

It was pointed out to me by a friend that one thing to consider when developing any website, isaccessability. This can relate to responsive design, so that mobile users can access the website, however accessbility dhould be taken into account when developing the website for those with certain disabilities. Blind internet users are able to use features provided on certain websites such as Wikipedia that allow them to play audio recordings of pages and articles. Some websites are also developed to be Autism friendly, and avoid using loud sounds and large and distracting images. Some websites might also take care to remove flashing and strobing images and effects to cater to sufferers of Epilepsy. When developing my website, I didn't take into account accessbility for disabled users. This should be especially important for an application such as mine, where it's main purpose is to help people purchase medical supplies online. A large consumer demographic would therefore include people who cannot, or struggle to visits Doctors and Pharmacys. In the future, I should consider this audience, and tailor the website to incude more features that would suite their needs.



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
