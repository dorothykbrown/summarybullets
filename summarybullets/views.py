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

    summary_serializer = SummarySerializer(data=summary_data)
    if summary_serializer.is_valid():
        summary_serializer.save()
        return Response(summary_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(summary_serializer.data)

def summary_detail(request, pk):
    '''Returns summary'''

    try:
        summary = Summary.objects.get(pk=pk)
    except Summary.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SummarySerializer(summary)
        return JsonResponse(serializer.data)


def summaries(request):
    '''Shows all summaries'''

    summaries = Summary.objects.all()
    summary_serializer = SummarySerializer(summaries, many=True)

    return JsonResponse(summary_serializer.data, safe=False)

@api_view(['POST'])
def generate_bullet_points(request):
    '''accepts text input and returns bullet points'''
    print("request: ", request)
    original_text = request.data
    bullet_point_data = get_bullet_point_data(original_text)

    bp_serializer = BulletPointSerializer(data=bullet_point_data)
    if bp_serializer.is_valid():
        bp_serializer.save()
        return Response(bp_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(bp_serializer.data)

def bullet_points(request, pk=None):
    '''shows all bullet points, or the details of one bullet point if a pk is provided'''

    if pk is not None:
        print("pk: ", pk)
        try:
            bullet_point = BulletPoint.objects.get(pk=pk)
        except BulletPoint.DoesNotExist:
            return HttpResponse(status=404)

        serializer = BulletPointSerializer(bullet_point)
        return JsonResponse(serializer.data)
    
    bullet_points = BulletPoint.objects.all()
    bullet_point_serializer = BulletPointSerializer(bullet_points, many=True)
    return JsonResponse(bullet_point_serializer.data, safe=False)
