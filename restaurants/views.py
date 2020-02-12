from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list": [
    {"restaurant_name":"Macdonalds",
     "food_type" : "Junk Food",
     },

     {"restaurant_name" : "Buffalo Wings",
      "food_type" : "Wings",
      },

      {"restaurant_name" : "Al Quds",
       "food_type" : "Mansaf For Hamza",
      },
    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{"restaurant_name": "99 Grill",
                 "food_type" : "Burgers",
                 },


                 }

    return render(request, 'detail.html', context)
