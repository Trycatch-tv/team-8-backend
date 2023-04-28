from django.urls import path

from .views import *

urlpatterns=[
        #add Urls Actions
        path('add_student/', add_student.as_view(), name='add_student'),
        path('add_teacher/', add_teacher.as_view(), name='add_teacher'),
        path('add_course/', add_course.as_view(), name='add_course'),
        #List Urls Actions
        path('list_students/',student_list.as_view(),name="students_people"),
        path('list_courses/',course_list.as_view(),name="courses_people"),
        path('list_teachers/',teacher_list.as_view(),name="teachers_people"),
        #Update Urls Actions
        path('update_student/<int:pk>/', update_student.as_view(), name='update_student'),
        path('update_teacher/<int:pk>/', update_teacher.as_view(), name='update_teacher'),
        path('update_course/<int:pk>/', update_course.as_view(), name='update_course'),
        #Delete Urls Actions
        path('delete_student/<int:pk>/', delete_student.as_view()),
        path('delete_teacher/<int:pk>/', delete_teacher.as_view()),
        path('delete_course/<int:pk>/', delete_course.as_view()),
        #Login 
        path('user-login/', UserLoginAPIView.as_view(), name='user_login_api'),
        path('student-login/', StudentLoginView.as_view(), name='student_login_api'),
        path('teacher-login/', TeacherLoginView.as_view(), name='teacher_login_api'),
        
        #Relations
        path('profesores/<int:id>/estudiantes/', TeacherStudent.as_view(), name='profesor-estudiantes'),

        #get relations
        #path('teacher-student/<int:pk>/', TeacherStudent.as_view(),name="teacher_student"),
        path('api/estudiantes/<int:estudiante_id>/cursos/', CursosEstudianteView.as_view(), name='cursos_estudiante'),        
        path('agregar_curso_profesor_a_estudiante/', agregar_curso_profesor_a_estudiante, name='agregar_curso_profesor_a_estudiante'),


        path('agregar_curso_profesor/', agregar_curso_profesor, name='agregar_curso_profesor_a_estudiante'),
        path('api/profesor/<int:profesor_id>/cursos/', ProfesorCursosView.as_view(), name='cursos_profesores'),   
        
        
        path('api/profesores/<int:profesor_id>/estudiantes/', ProfesorEstudiantes.as_view(), name='estudiantes_profesores'),   
        
        
        
        
            
]