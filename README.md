# Project 4 - E-Commerce

Medical e-commerce website built using Django, Python, Javascript, HTML and CSS.

## Table of Contents  
1. [Deployment](#Deployment)  
2. [Testing](#Testing) 
3. [Goals](#Goals)
4. [Improvements](#Improvements)
5. [Credits](#Credits)

## Deployment <a name="Deployment"></a> 

The application has been deployed through Heroku. The live website can be accessed at: https://medicine-cabinet-js.herokuapp.com/
Due to unknown reasons, the application does not seem to work on Vivaldi browsers. After investigating the issue, I have not been able to find a clear reason as to why the website sometimes fails to load on Vivaldi. This could be a bug within Vivaldi itself, as the website works fine on other Browsers.
![Vivaldi Error](https://i.imgur.com/YT87yK7.png)

For the live version of this website, I have disabled debugging mode in my Django application settings by changing ```DEBUG = True``` to False. This means that the user won't see Django error messages (like the above) if the page fails to load for whatever reason, they will instead see regular HTTP errors, such as 404 not found for example.

To deploy the website, I deployed via the master Github branch through Heroku. To do this, I went into the Deployment section of my Heroku application settings, selected Master branch under manual deployment, and deployed from there. I also added my secret keys and URLs to my Heroku config variables, and then removed the hard-coded values from my code. This was done for security purposes.

## Testing <a name="Testing"></a>

In order to test my application, I used Djangos in-built testing framework. I created separate test files for different sections of my application, such as the payment form, account creation, and product selection.

```
    def test_no_submit_without_name(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        
    def test_no_submit_without_credit_card(self):
        form = MakePaymentForm({'Credit card number': ''})
        self.assertFalse(form.is_valid())
```
Here I have created tests for the payment form, to check if the form can be submitted under certain conditions, like whether or not the form can be submitted without certain fields like name and the credit card information. Having tests for my payment details form was useful when working with the Stripe API, as I was able to test for error before writing my actual error codes for the end user.

As with any website, I also tested it for responsiveness and usability on other devices. My images and text scaled appropriately when re-sized, and the interactive menu also changed to adapt to mobile devices and smaller screens by scaling into an accordion dropdown. This prevents the menu from obscuring any information when displayed on a small screen or mobile device. As mentioned above, the website sometimes fails to load on Vivaldi, however, I believe this may be a bug (this has also been discussed with other developers).

I also tested my Javascript, such as the code that controls the modal. when I first implemented the modal I just wanted to see how the modal would look on my website, so before associating any kind of button with it, I created the script to run whenever I clicked on the window, and I created the button for the modal later on once i was satisfied with the modal itself.

```
window.onclick = function() {
  modal.style.display = "block";
};
```
Doing this meant I could focus on implementing the initial mdal functionality, then improve it, all before worrying about how the end user would activate it (in the end I settled for a button in the nav bar).

## Goals <a name="Goals"></a>

The idea for this website is to make buying/paying for medication easier for people. Right now most people pick up their medicine from a pharmacist or doctor's practice, but I think in the future medication will be bought online by most people, for its convenience. I think a lot of older people could benefit from such a website. With that in made, I have made the website easy to use, from selecting items, all the way to paying for them. I have included a FAQ modal as well which contains all the details about the website. 

I have created a wireframe which outlines the details for the website. I think the final product turned out a lot like my wireframe which I'm happy with. I would have liked to have the products wrapped in their own individual containers, which would allow users to scrolls through the listings without scrolling through the page itself. This would have meant that the nav bar would remain on screen at all times. Apart from that, I think the website is faithful to the wire frame that I created.

![Wireframe](https://i.imgur.com/JOSkyRd.png)

I wanted my website to have a tutorial/FAQ popup that wouldn't be too intrusive. One of my main goals was to make the website easy to use, and having a simple to use FAQ section was something that I wanted to use from the very start of development. I chose to use a modal rather than a separate page, as this allowed users to view the FAQ, without losing their cart, or their place on the page. This meant that a user could easily open and close the FAQ without disruption, and overall I think it works very well with the clean and concise theme of the website.

I looked at other medical supplier websites and I found that many include the design concepts that I had envisioned for my own website. They were sleek, simple to use and modern looking. I wanted my website to have a clinical and professional review. I also looked at other medical websites that weren't related to e-commerce, such as WebMD and the NHS website. I found that even though these websites were not related to shopping, they still shared many themes and design choices that medical e-commerce sites had in their design.

![Example ecommerce site](https://i.imgur.com/m7Wt0NW.png)


## Improvements <a name="Improvements"></a>

It was pointed out to me by a friend that one thing to consider when developing any website, accessibility. This can relate to responsive design so that mobile users can access the website, however, accessibility should be taken into account when developing the website for those with certain disabilities. Blind internet users are able to use features provided on certain websites such as Wikipedia that allow them to play audio recordings of pages and articles. Some websites are also developed to be Autism friendly, and avoid using loud sounds and large and distracting images. Some websites might also take care to remove flashing and strobing images and effects to cater to sufferers of Epilepsy. When developing my website, I didn't take into account accessibility for disabled users. This should be especially important for an application such as mine, where the main purpose is to help people purchase medical supplies online. A large consumer demographic would, therefore, include people who cannot, or struggle to visits Doctors and Pharmacies. In the future, I should consider this audience, and tailor the website to include more features that would suit their needs.

Including some more Javscript for added user interactivity might have been a useful addition. There are tools such as introJS which can create more guided user experiences. For my application I did try to incorporate this, however it produced a lot of issues and I wasn't able to get it working. It was also suggested to me to my modal accomplishes most of the same functionality that introJS would have done, so I think the trade-off isn't too massive, and the modal fills in a lot of the design space that an interactive tutorial would have done.


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
