import os
import shutil

from flask import Flask
from flask import url_for
from flask import request


app = Flask(__name__)


@app.route('/')
def func():
    return "<strong>Миссия Колонизация Марса</strong>"


@app.route('/index')
def index():
    return "<strong>И на Марсе будут яблони цвести!</strong>"


@app.route("/promotion")
def promotion():
    return """<b>Человечество вырастает из детства.<br>
              Человечеству мала одна планета.<br>
              Мы сделаем обитаемыми безжизненные пока планеты.<br>
              И начнем с Марса!<br>
              Присоединяйся!</b>"""


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <figure>
                        <figcaption>
                            <img src="{url_for('static', filename='img/mars.jpg')}" width="100%" alt="Картика">
                        </figcaption>
                            <p>Вот она какая, красная планета.</p>
                    </figure>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" href="/static/css/style.css" type="text/css" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>

                    <img src="{url_for('static', filename='img/mars.jpg')}" alt="Картика" width="100%">

                    <div id="a1" class="alert alert-dark" role="alert">
                      <strong>Человечество вырастает из детства.</strong>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <strong>Человечеству мала одна планета.</strong>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <strong>Мы сделаем обитаемыми безжизненные пока планеты.</strong>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <strong>И начнём с Марса!</strong>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <strong>Присоединяйся!</strong>
                    </div>
                  </body>
                </html>'''


@app.route("/astronaut_selection", methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static',
                                                                                  filename='css/styles.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претиндента</h1>
                            <h2 align="center">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя">
                                    <p></p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">

                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее (бакалавриат/специалитет)</option>
                                          <option>Высшее (магистратура)</option>
                                        </select>
                                     </div>


                                    <div class="form-group">
                                        <label for="form-check">Какие у Вас есть професии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="eng-expl" id="eng-expl">
                                          <label class="form-check-label" for="defaultCheck1">
                                            Инженер-исследователь
                                          </label><br>

                                          <input class="form-check-input" type="checkbox" value="eng-build" id="eng-build">
                                          <label class="form-check-label" for="defaultCheck2">
                                            Инженер-строитель
                                          </label><br>

                                          <input class="form-check-input" type="checkbox" value="pilot" id="pilot">
                                          <label class="form-check-label" for="defaultCheck3">
                                            Пилот
                                          </label><br>

                                          <input class="form-check-input" type="checkbox" value="meteo" id="meteo">
                                          <label class="form-check-label" for="defaultCheck4">
                                            Метеоролог
                                          </label><br>

                                          <input class="form-check-input" type="checkbox" value="eng-live" id="eng-live">
                                          <label class="form-check-label" for="defaultCheck5">
                                            Инженер по жизнеобеспечению
                                          </label><br>

                                          <input class="form-check-input" type="checkbox" value="eng-save" id="eng-save">
                                          <label class="form-check-label" for="defaultCheck6">
                                             Инженер по радиационной защите
                                          </label><br>

                                          <input class="form-check-input" type="checkbox" value="medic" id="medic">
                                          <label class="form-check-label" for="defaultCheck7">
                                           Врач
                                          </label><br>

                                          <input class="form-check-input" type="checkbox" value="exobio" id="exobio">
                                          <label class="form-check-label" for="defaultCheck8">
                                           Экзобиолог
                                          </label><br>
                                        </div>
                                    </div>

                                    <p></p>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>

                                    <p></p>

                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>

                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>

                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return """<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <title>Пройдено!</title>
                          </head>
                          <body>
                            <div class="alert alert-warning" role="alert">
                                <b>Форма отправлена!</b>
                            </div>
                          </body>
                        </html>
    """


@app.route("/choice/<planet_name>")
def choice(planet_name):
    facts = []
    if planet_name == "Венера":
        facts.append('Почти такие же размеры и масса как и у Земли,'
                     ' год на 40% короче земного, а гравитация - 90% от земной.')
        facts.append(' До Венеры попросту меньше лететь.'
                     ' Среднее расстояние от Земли до Венеры'
                     ' - 108 млн км, а до Марса - 225 млн км.')
        facts.append('На Венере нет смены времён года, а значит нам не придётся мёрзнуть зимой!')
        facts.append('Красота пейзажа Венеры несравнима ни с чем!')

    return f''' <!DOCTYPE html>
                <html>
                <head>
                    <title>Варианты выбора</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                     href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                     integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                     crossorigin="anonymous">
                     <link rel="stylesheet" type="text/css" href="{url_for('static',
                                                                           filename='css/special-style.css')}">
                </head>
                <body>
                    <div class="container">
                        <header>
                            <h1>Моё предложение: Венера</h1>
                        </header>
                        <div class="reason1">
                            <p class="first">{facts[0]}</p>
                        </div>

                        <div class="reason2">
                            <p class="second">{facts[1]}</p>
                        </div>

                        <div class="reason3">
                            <p class="third">{facts[2]}</p>
                        </div>

                        <div class="reason4">
                            <p class="fourth">{facts[3]}</p>
                        </div>
                    </div>
                </body>
                </html>
                        '''


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                   integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                   crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <div class="alert alert-success" role="alert">
                      <b>Поздравляем! Ваш рейтинг после {level} отбора</b>
                    </div>
                    <h4>составляет {rating}!</h4>
                    <div class="alert alert-warning" role="alert">
                      <b>Желаем удачи!</b>
                    </div>
                  </body>
                </html>'''


@app.route("/load_photo", methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f''' <!doctype html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/sty.css')}"/>
                        </head>
                        <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h2 align="center">для участия в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                        </body>
                    </html>
                    '''
    elif request.method == 'POST':
        try:
            f = request.files['file']
            with open("photo.jpg", "wb") as file:
                file.write(f.read())
            try:
                os.remove("static/img/photo.jpg")
            except BaseException:
                pass
            shutil.move("photo.jpg", "static/img/photo.jpg")
            return f''' <!doctype html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static',
                                                                                  filename='css/sty.css')}"/>
                            </head>
                            <body>
                                <h1 align="center">Загрузка фотографии</h1>
                                <h2 align="center">для участия в миссии</h2>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                            <img src="{url_for('static',
                                                               filename='img/photo.jpg')}" alt="Картинка" width="100%">
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                            </body>
                        </html>
                        '''
        except:
            return f''' <!doctype html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/sty.css')}"/>
                        </head>
                        <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h2 align="center">для участия в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                        </body>
                    </html>
                    '''


@app.route("/carousel")
def carousel():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="../static/css/car.css" />
                        <title>Пейзажи Марса</title>
                      </head>
                      <body>
                        <h1 align="center">Пейзажи Марса</h1>


                        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                          <ol class="carousel-indicators">
                            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                          </ol>
                          <div class="carousel-inner">
                            <div class="carousel-item active">
                              <img class="d-block w-100" src="../static/img/fon1.jpg" alt="First">
                            </div>
                            <div class="carousel-item">
                              <img class="d-block w-100" src="../static/img/fon2.jpg" alt="Second">
                            </div>
                            <div class="carousel-item">
                              <img class="d-block w-100" src="../static/img/fon3.jpg" alt="Third">
                            </div>
                          </div>
                          <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="sr-only">Previous</span>
                          </a>
                          <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                          </a>
                        </div>
                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
