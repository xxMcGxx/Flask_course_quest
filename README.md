# Flask_course_quest

Учебный проект для платформы Stepik
Для CSS использовался фреймворк Bootstrap4 в виде модумя bootstrap-flask
Из-за особенностей данного модуля в шаблонах присутствуют импорты макросов из папки Templates/Bootstrap при отсутствии оной в проекте, это нормальное поведение для данного фреймворка, т.к. роуты к темплейтам прописываются при создании объекта Bootstrap, и загружаются или с сети или локально из site-packeges, я поставил локальную подгрузку стилей. 
