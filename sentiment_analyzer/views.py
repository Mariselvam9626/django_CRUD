from rest_framework.views import APIView
from rest_framework.response import Response
from textblob import TextBlob

class EmojiAPIView(APIView):

    def post(self, request):
        text = request.data.get("text")

        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0.5:
            emoji = "😀🎉"
        elif polarity > 0:
            emoji = "🙂👍"
        elif polarity < -0.5:
            emoji = "😢💔"
        elif polarity < 0:
            emoji = "😠"
        else:
            emoji = "😐"

        return Response({
            "text": text,
            "emoji": emoji,
            "polarity": polarity
        })