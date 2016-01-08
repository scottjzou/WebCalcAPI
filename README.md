# WebCalcAPI
A Django Rest Framework Site that provides online calculation functions through API calls. Also a guide on how to create multiple versions of django-rest-framework APIs.

Author: [Jiahang Zou](https://github.com/scottjzou)

## Requirements
Install by running `pip install -r requirements.txt`

* Required:
	* Django==1.9.1
	* djangorestframework==3.3.2
* Optional:
	* django-rest-swagger==0.3.4 (prereq: PyYAML==3.11)
	* To run `asian_option` example: 
		* numpy==1.10.4
		* scipy==0.16.1
		
* The versions are not strictly required, as the author simply used the newest version there is through pip install.
* **django-rest-swagger** is an api documentation generator that is quite useful if this project becomes large-scale. However, the base status of the version is not implementing it, as it is for internal use.

## Structure
Notice this is a django-project, so it obeys all the django rules. For details, see <https://www.djangoproject.com/>.

The APIs in this project is primarily for temporary calculation purposes, instead of retrieving objects from object models. Therefore, function-based views were used to design such models.

Under [views.py](WebCalculator/views.py), there are example functions of api views. Each of these is a function dealing with get requests, with related urls under [urls.py](WebCalculator/urls.py). For more details, read the documentations under each function.

## Adding another function

1. Define the function in [views.py](WebCalculator/views.py), follow the format of other functions (e.g. with api_view decorator, a description of input and output types, a try/except clause), and by taking a request and examing its arguments, return a Response object.
2. Add a url with the desired format in [urls.py](WebCalculator/urls.py)
3. Add your new function in api_root under [views.py](WebCalculator/views.py). Make sure the name your reverse matches the name you give in urls.py in step 2.
4. Testing: To run a local server, do `python manage.py runserver` at the base directory, and then check your localhost at port 8000: <http://localhost:8000>, your API should be linked there, or directly call your API with your given format.


