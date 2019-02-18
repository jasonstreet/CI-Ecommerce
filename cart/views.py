from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """
    Renders cart content
    """
    return render(request, 'cart.html')
    
def add_to_cart(request, id):
    """
    Add a quantity of product to cart
    """
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))
    
def adjust_cart(request, id):
    """
    Adjust quantity of product in cart by a certain amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))