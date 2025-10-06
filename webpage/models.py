from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    """ท่าออกกำลังกาย"""
    DIFFICULTY_CHOICES = [
        ('เริ่มต้น', 'เริ่มต้น'),
        ('ปานกลาง', 'ปานกลาง'),
        ('ยาก', 'ยาก'),
    ]
    
    TYPE_CHOICES = [
        ('แขน', 'แขน'),
        ('ขา', 'ขา'),
        ('อก', 'อก'),
        ('หลัง', 'หลัง'),
        ('ไหล่', 'ไหล่'),
        ('หน้าท้อง', 'หน้าท้อง'),
        ('คาร์ดิโอ', 'คาร์ดิโอ'),
        ('ยืดเหยียด', 'ยืดเหยียด'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=200, verbose_name='ชื่อท่า')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name='ประเภท')
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES, verbose_name='ระดับความยาก')
    description = models.TextField(blank=True, verbose_name='คำอธิบาย')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'ท่าออกกำลังกาย'
        verbose_name_plural = 'ท่าออกกำลังกาย'
    
    def __str__(self):
        return f"{self.name} ({self.type})"


class WorkoutProgram(models.Model):
    """โปรแกรมออกกำลังกาย"""
    GOAL_CHOICES = [
        ('ลดน้ำหนัก', 'ลดน้ำหนัก'),
        ('เพิ่มกล้ามเนื้อ', 'เพิ่มกล้ามเนื้อ'),
        ('เสริมความแข็งแรง', 'เสริมความแข็งแรง'),
        ('เพิ่มความอดทน', 'เพิ่มความอดทน'),
        ('เพิ่มความยืดหยุ่น', 'เพิ่มความยืดหยุ่น'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(max_length=200, verbose_name='ชื่อโปรแกรม')
    goal = models.CharField(max_length=100, choices=GOAL_CHOICES, verbose_name='วัตถุประสงค์')
    exercises = models.ManyToManyField(Exercise, related_name='programs', verbose_name='ท่าออกกำลังกาย')
    description = models.TextField(blank=True, verbose_name='คำอธิบาย')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'โปรแกรมออกกำลังกาย'
        verbose_name_plural = 'โปรแกรมออกกำลังกาย'
    
    def __str__(self):
        return self.name


class WorkoutLog(models.Model):
    """บันทึกการออกกำลังกาย"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_logs')
    date = models.DateField(verbose_name='วันที่')
    duration = models.IntegerField(verbose_name='ระยะเวลา (นาที)')
    program = models.ForeignKey(WorkoutProgram, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='โปรแกรม')
    notes = models.TextField(blank=True, verbose_name='บันทึก')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = 'บันทึกการออกกำลังกาย'
        verbose_name_plural = 'บันทึกการออกกำลังกาย'
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"


class WorkoutLogExercise(models.Model):
    """ท่าที่ทำในแต่ละบันทึก"""
    workout_log = models.ForeignKey(WorkoutLog, on_delete=models.CASCADE, related_name='log_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField(default=0, verbose_name='เซ็ต')
    reps = models.IntegerField(default=0, verbose_name='ครั้ง/เซ็ต')
    weight = models.DecimalField(max_digits=5, decimal_places=1, default=0, verbose_name='น้ำหนัก (kg)')
    
    def __str__(self):
        return f"{self.exercise.name} - {self.sets}x{self.reps}"