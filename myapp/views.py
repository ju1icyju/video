from django.conf import settings
from moviepy.editor import *
from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage


def create_video(request):
    if request.method == 'GET':
        text = request.GET.get('text', '')
        video_path = os.path.join(settings.STATIC_ROOT, 'video/video_test.mp4')
        video = VideoFileClip(video_path)                                                                               #  изначальное видео на которое ссылаемся

        txt_clip = ( TextClip(text,fontsize=30,color='white')
                   .set_position(lambda t: (max(0, video.w - 50*t), 'center'))
                   .set_duration(video.duration)
                   .crossfadein(0.5)
                   .crossfadeout(0.5)
                   .set_start(0) )
                                                                                                                        # настройка текста
        video = CompositeVideoClip([video, txt_clip], size=(100, 100))
        output_path = os.path.join(settings.STATIC_ROOT, 'video/video_output.mp4')
        video.write_videofile(output_path, codec="mpeg4")
        return render(request, 'video_created.html', {'text': text})
                                                                                                                        # склеиваем и сохраняем