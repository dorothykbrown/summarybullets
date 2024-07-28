from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BulletPoint, Summary
from .serializers import BulletPointSerializer, SummarySerializer
from .groq_service import get_bullet_point_data, get_text_summary_data
from rest_framework.renderers import JSONRenderer


@api_view(['POST'])
def generate_summary(request):
    '''Accepts text input and returns serialized summary object'''

    original_text = request.data
    summary_data = get_text_summary_data(original_text)

    serializer = SummarySerializer(data=summary_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return JsonResponse(serializer.data)

def summaries(request, pk=None):
    '''Shows all Summaries or the details of a Summary if a pk is provided.'''

    if pk is not None:
        try:
            summary = Summary.objects.get(pk=pk)
        except Summary.DoesNotExist:
            return HttpResponse(status=404)
        
        if request.method == 'GET':
            serializer = SummarySerializer(summary)
            return JsonResponse(serializer.data)

    summaries = Summary.objects.all()
    serializer = SummarySerializer(summaries, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def generate_bullet_points(request):
    '''Accepts text input and returns a serialized BulletPoint object'''

    original_text = request.data
    bullet_point_data = get_bullet_point_data(original_text)

    serializer = BulletPointSerializer(data=bullet_point_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.data)

def bullet_points(request, pk=None):
    '''Shows all BulletPoints, or the details of one BulletPoint if a pk is provided'''

    if pk is not None:
        try:
            bullet_point = BulletPoint.objects.get(pk=pk)
        except BulletPoint.DoesNotExist:
            return HttpResponse(status=404)

        serializer = BulletPointSerializer(bullet_point)
        return JsonResponse(serializer.data)
    
    bullet_points = BulletPoint.objects.all()
    serializer = BulletPointSerializer(bullet_points, many=True)

    return JsonResponse(serializer.data, safe=False)
