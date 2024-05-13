from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import jwt
import os
import shutil
import traceback

def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def retrieve_json_and_get_data(request):
    if request.method == 'POST' and request.FILES.get('myFile'):
        try:
            uploaded_file = request.FILES['myFile']
            print("Starting")
            save_directory = r"generate_data"
            os.makedirs(save_directory, exist_ok=True)  # Create the directory if it doesn't exist

            file_path = os.path.join(save_directory, uploaded_file.name)
            print("File path:", file_path)
            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # Remove the existing directory
            try:
                shutil.rmtree("generate_data/twitter_data")
            except Exception as e:
                pass

            # Process the uploaded file
            from generate_data import data
            data.twitter_account_data()

            # Load JSON data from the generated file
            with open(r"generate_data/data.json") as json_file:
                jsonData = json.load(json_file)

            # Clear the contents of the JSON file
            with open(r"generate_data/data.json", 'w') as f:
                json.dump({}, f)

            return JsonResponse({"jsonData": jsonData, 'message': 'File processed successfully.'})
        except Exception as e:
            print("Error:")
            traceback.print_exc()
            return JsonResponse({'error': 'Failed to process the file.'}, status=500)
    else:
        print("Error: No file uploaded or invalid request method.")
        return JsonResponse({'error': 'No file uploaded or invalid request method.'}, status=400)
