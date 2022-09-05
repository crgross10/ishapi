Como rodar o projeto? <br>

1. Clone esse repositório: <br>
  - git clone https://github.com/crgross10/projeto-vaga-backend-master.git <br>

2. Crie um virtualenv com Python 3: <br>
  - pip3 install virtualenvwrapper  (OBS: WINDOWS 10 ---> virtualenvwrapper-win ) <br>
  - mkvirtualenv <nome_para_virtual_env> <br>

3. Ative o virtualenv: <br>
  - workorn  <nome_da_virtual_env_criada_passo_anterior> <br>

4. Instale as dependências: <br>
  - pip install -r requirements.txt <br>

5. Rode as migrações: <br>
  - python manage.py makemigrations <br>
  - python manage.py migrate <br>

6. Swagger: <br>
  - http://localhost:8000/

7. Listagem de departamentos: <br>   
  - http://localhost:8000/api/departamentos/

8. Consultar todos os colaboradores de um departamento:  <br>
  - http://localhost:8000/api/departamento/<id_departamento>/  <br>
    Ex: http://localhost:8000/api/departamento/1/
