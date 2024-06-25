import boto3
import json
from django.http import JsonResponse
from django.views import View

class PredictView(View):
    def post(self, request, *args, **kwargs):
        # Parse the input data from the request
        input_data = json.loads(request.body)

        # AWS SageMaker client
        client = boto3.client('sagemaker-runtime', region_name='YOUR_AWS_REGION')

        # Name of the deployed endpoint
        endpoint_name = 'YOUR_SAGEMAKER_ENDPOINT_NAME'

        # Convert input data to JSON
        payload = json.dumps(input_data)

        # Send the request to the SageMaker endpoint
        response = client.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='application/json',
            Body=payload
        )

        # Read the response
        result = json.loads(response['Body'].read().decode())

        # Return the response as JSON
        return JsonResponse(result)