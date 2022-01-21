from rest_framework import serializers

from db_course_work_backend.models import EXCURSION, GROUP, EXCURSIONIST, PERSONAL_DATA, GUIDE, PASSPORT


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PASSPORT
        fields = ["NAME", "SURNAME"]


class GuideSerializer(serializers.ModelSerializer):
    PASSPORT_ID = PassportSerializer()

    class Meta:
        model = GUIDE
        fields = ['PASSPORT_ID']


class GroupSerializer(serializers.ModelSerializer):
    GUIDE = GuideSerializer()
    free_slots = serializers.SerializerMethodField()

    def get_free_slots(self, obj):
        return obj.NUMBER_SEATS - obj.excursionist.count()

    class Meta:
        model = GROUP
        fields = ['GUIDE', 'TIME', 'COST', 'NUMBER_SEATS', 'free_slots', 'id']


class FullExcursionSerializer(serializers.ModelSerializer):
    museum = serializers.StringRelatedField(many=True)
    exhibition = serializers.StringRelatedField(many=True)
    exhibit = serializers.StringRelatedField(many=True)
    group_set = GroupSerializer(many=True)

    class Meta:
        model = EXCURSION
        fields = ['NAME', 'DESCRIPTION', 'DURATION', 'museum', 'exhibition', 'exhibit', 'group_set']


class SmallExcursionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EXCURSION
        fields = ['NAME', 'DESCRIPTION', 'DURATION', "id"]
