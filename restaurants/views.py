from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {

    	"my_list": [

    {
    	"restaurant_name": "KFC",
    	"food_type": "fried chicken",
    },

    {
    	"restaurant_name": "pick",
    	"food_type": "frozen yoghurt",

    },

    {
    	"restaurant_name": "cucou",
    	"food_type": "fries"
    },

    ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {

    "my_object": 

    {
    	"restaurant_name": "KFC",
    	"food_type": "fried chicken",
    },


    }
    return render(request, 'detail.html', context)
