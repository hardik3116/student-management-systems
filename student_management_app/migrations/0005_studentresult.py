

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0004_auto_20200703_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_exam_marks', models.FloatField(default=0)),
                ('subject_assignment_marks', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.Students')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.Subjects')),
            ],
        ),
    ]
