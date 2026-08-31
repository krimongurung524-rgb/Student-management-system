from django import template

register = template.Library()


# Filter — to make grade display more better
@register.filter
def grade_label(grade):
    labels = {
        'grade_9': 'Grade 9',
        'grade_10': 'Grade 10',
        'grade_11': 'Grade 11',
        'grade_12': 'Grade 12',
    }
    return labels.get(grade, grade)


# Simple tag 
@register.simple_tag
def gender_icon(gender):
    icons = {
        'male': '👨',
        'female': '👩',
        'other': '🧑',
    }
    return icons.get(gender.lower(), '🧑')