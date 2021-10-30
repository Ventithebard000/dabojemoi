






init:
    python:
        def max_points(*values):
            return [ i for i, v in enumerate(values) if v == max(values) ]
    $ quiz_score = 0


define s = Character(" ")
define p = Character("[povname]")
define a = Character(" ", what_color="ffffff")
define m = Character(" ", what_color="f60609")
define b = Character("Шин", what_font="cabinvariable.ttf", what_color="ffffff", window_background="textboxnew.png")
define w = Character("???", what_font="cabinvariable.ttf", what_color="ffffff", window_background="textboxnew.png")
define c = Character("Соу", what_font="cabinvariable.ttf", what_color="ffffff", window_background="textboxnew.png")
define pov = Character(" ", what_font="cabinvariable.ttf", what_color="ffffff", window_background="textboxnew.png")



label start:





        $ points = 50
    $ name_list = ["соу", "хиёри", "соу хиёри", "хиёри соу", "СОУ", "ХИЁРИ", "ХИЁРИ СОУ", "СОУ ХИЁРИ"]





    play music tansaku3 fadein 2
    scene bg black
    pause(2.0)



    a "> Когда остальная часть группы исследовала этаж, ты решила рискнуть и остаться позади."

    a "> Ты недавно заметила эту комнату в углу коридора, но другие решили игнорировать её по некоторым причинам."

    a "> Может быть это не плохая идея, чтобы зайти внутрь и поискать там, пока остальных нет."

    a "> Ты замедляешь свой шаг, затем полностью поворачиваешь назад."

    a "> К счастью, дверь была не заперта."

    scene bg monitor room
    with dissolve

    a "> . . . ."

    a "> Сначала ты не увидела ничего интересного... или опасного, пока что."

    a "> Комната была заполнена мониторами и кнопками, так же куча другим техническим оборудованием ."

    a "> Выглядит как комната Мастера этажа."

    a "> Может быть ты могла  попробовать взломать систему... Но это было слишком смелое утверждение. "

    a "> Вероятно, для этого понадобиться больше, чем просто пароль."

    a "> Ты решила тщательно обыскать комнату, пока другие не нашли тебя. У тебя было не так много времени."

    scene bg monitor room 1
    with hpunch

    play sound computer

    a "> . . . ?"

    a "> Хм?"

    stop music fadeout 2

    a "> Монитор...включен?"

    a "Посмотреть туда?"

    menu:
        "> Да":


            a "> Ты осторожно приближаешься к экрану."

            "'Ох, нет. Ты не... Кто ты? Ты не должна быть здесь...'"

            a "> Похоже, голос идёт из монитора."

            scene mon red
            with dissolve

            a "> Приблизившись к экрану, ты не ожидала увидеть лицо."

            play sound computer
            scene mon shin
            with hpunch
            pause (1.0)



            "'П-пожалуйста, покинь эту комнату... У тебя будут проблемы! Если ты уйдёшь прямо сейчас, я ни кому не скажу, что ты была здесь, я обещаю.'"
        "> Нет":

            a "> Ты решила заняться своими делами. Это могло быть ловушкой."

            a "> Закончив исследовать комнату без прикосновения к чему-то, ты уже собиралась уходить."

            a "> Но затем... Услышала голос."

            scene mon red
            with dissolve
            pause (0.5)

            play sound computer
            scene mon shin
            with hpunch
            pause (1.0)



            "'Эм... Хиёри, это ты?'"

    menu:
        "> Это ловушка?":
            a "> Ты придвигаешь стул ближе к рабочему монитору, чтобы сесть."

            a "> Ты уже видела ИИ до этого, и этот вероятно не причинит тебе вреда. По крайне мере, не слишком сильно."

            "'Я... Я не понимаю о чём ты говоришь...'"

            "'Эта комната может быть опасной, но не из-за меня...'"

            "'Я имею в виду, я был бы рад помочь, если что нибудь случилось... Я смогу сделать это!'"

            "'Ох! То есть! Я не говорю, что должно что-то произойти..!'"

            jump who
        "> Кто ты?":

            jump who


    label who:

    scene bg neutral
    with dissolve

    show neutral1
    with dissolve

    stop music fadeout 1
    play music denpa

    "'Я.. Я просто обычный человек... ИИ, точнее... Ты друг Хиёри?'"

    "'Он сказал, что кто-то должен прийти... Но я не думал, что это будет только один человек.'"

    hide neutral1
    show sad2

    "'Может.. что-то произошло...'"

    "'Если ты не одна, то тебе будет лучше вернуться к другим... Быть здесь одной - очень опасно...'"

    menu:
        "> Это очень мило с твоей стороны":
            $ points += 1
            show bg love with dissolve

            hide sad2
            show shock1
            "'Мило? П-почему... Ты не должна...'"

            "'Я просто... Я просто хочу помочь... Я против жестокости.'"

            "'Я действительно не могу рассказать много чего, но я не наврежу тебе...'"
        "> Кто-то был здесь до меня?":




            $ points += 0

            show bg neutral with dissolve

            hide sad2
            show neutral1

            "'Нет, не совсем...'"

            "'Никого не было здесь... до тебя...'"

            "'Честно, я был здесь один долгое время и...'"

            "'Я не должен говорить с тобой, но... Мне жаль, просто... тут так тихо...'"
        "> Если это ловушка, то самая идиотская":



            $ points -= 1

            show bg bad with dissolve

            show nerv1

            "'Что? Я-я имею в виду, мы с тобою здесь на равных, я...'"

            "'Я просто... Я просто пытаюсь помочь... Я против жестокости.'"

            hide nerv1
            show sad2

            "'Я правда не могу рассказать тебе многого, но я не наврежу тебе...'"


    show bg neutral with dissolve

    show neutral2

    "'Ох! Я забыл представиться!..'"

    hide neutral2
    show happ1

    "'Меня зовут Шин...'"

    hide happ1
    show happ3

    "'Прости, если прошу слишком много... Ты могла бы сказать своё имя тоже?'"

    hide happ3
    show neutral1

    "'Ты можешь держать это в секрете, если хочешь... Я не возражаю.'"

    label name:

    menu:
        "> Меня зовут...":
            $ points += 1
            $ nameset = True

            python:
                povname = renpy.input("Как тебя зовут?", length=32)
                povname = povname.strip()


            if povname in ["соу", "хиёри", "соу хиёри", "хиёри соу", "СОУ", "ХИЁРИ", "ХИЁРИ СОУ", "СОУ ХИЁРИ", "Соу", "Хиёри", "Соу Хиёри", "Хиёри соу"]:


                play sound accent401
                stop music
                show bg bad

                show scared1

                "'. . . .'"

                hide scared1
                show scared2

                "'Ч-....'"

                "'Ох...'"

                "'Я просто... Я не-'"

                hide scared2
                show scared1

                "'Извини, на секунду я просто...'"

                hide scared1
                show nerv1

                play music denpa fadein 1

                "'Ты уверена, что это твоё имя?'"

                menu:
                    "> Да":

                        hide nerv1
                        show scared2

                        "'...Понятно.'"

                        "'Это просто немного удивительно, вот и всё...'"

                        hide scared2
                        show nerv1

                        "'Но если это твоё имя, конечно...'"

                        "'Извини, я навёл столько суматохи...'"

                        hide nerv1
                        show happ4

                        "'Приятно познакомиться, [povname]!'"

                        show bg neutral with dissolve
                        hide happ4
                        show neutral2

                        "'Ты знаешь, это напомнило мне о том, когда я впервые услышал это имя...'"

                        "'У меня был один эм... один друг в школе тогда.'"

                        hide neutral2
                        show nerv1

                        "'К несчастью, наша дружба не продлилась долго и...'"

                        hide nerv1
                        show neutral1

                        "'Ох! Извини, ты наверное не заинтересована в этом.'"

                        "'Могу я тебе помочь в любом случае?'"

                        jump talk
                    "> Нет, я просто шучу":


                        hide nerv1
                        show shock1

                        "'Ох!'"

                        hide shock1
                        show nerv1

                        "'Это было не смешно!...'"

                        "'Но ты подловила меня, хаха...'"

                        "'Извини, я навёл столько суматохи...'"

                        show bg neutral with dissolve
                        hide nerv1
                        show happ3

                        "'Ты не против сказать своё настоящее имя?'"

                        "'Извини, если я слишком настаиваю...'"

                        hide happ3
                        show nerv1

                        "'Это совершенно понятно, если ты не захочешь делиться своей информацией с другими.'"



                        jump name

            elif povname in ["владыка", "Владыка"]:

                hide neutral1
                show shock1

                "'. . . .'"

                "'Точно?'"

                hide shock1
                show neutral2

                "'..Как скажешь...'"

                hide neutral2
                show nerv1

                "'Но только не при всех, л-ладно?'"

                "'. . . .'"

                hide nerv1
                show scared1

                "'Господи, за что мне это...'"

                "'. . . .'"

                hide scared1
                show nerv1

                "'Рад познакомиться, эээ... [povname].'"

                "'Сделаем вид, что этого не было.'"



                jump talk

            elif povname in ["мочезавры", "мочезавр", "Мочезавры", "Мочезавр", "Уринозавр", "уринозавр", "Уринозавры", "уринозавры"]:

                hide neutral1
                show shock1

                "'. . . .'"

                "'. . . .'"

                hide shock1
                show nerv1

                "'Здорово.'"

                "'Хочешь проверить мою способность логически мылить?'"

                "'Или можно сразу начинать звонить в органы пепеги?'"

                "'Рад познакомиться, эээ... [povname].'"

                "'Сделаем вид, что этого не было.'"



                jump talk
            else:



                show bg love with dissolve

                hide neutral1
                show happ2

                "'Спасибо!!'"

                "'[povname]!... Приятно познакомиться!'"

                jump fren

            label fren:


                show bg neutral with dissolve

                hide happ2
                show neutral2

                "'Ты знаешь, у меня раньше был друг с таким же именем...'"

                "'К несчастью, наша дружба не продлилась долго и...'"

                hide neutral2
                show nerv1

                "'Ох! Извини, ты наверное не заинтересована в этом.'"

                hide nerv1
                show neutral1

                "'Могу ли я тебе помочь в любом случае?'"

                jump talk
        "> Не думаю. Это может быть опасно.":

            $ points -= 1


            show bg bad with dissolve

            hide neutral1
            show sad1

            "'Ох... Окей...'"

            "'Ты знаешь... У меня был друг, который тоже всегда был очень осторжен...'"

            hide sad1
            show nerv1

            "'Ох! Извини, ты наверное не заинтересована в этом.'"

            hide nerv1
            show neutral1

            "'Могу ли я помочь тебе в любом случае?'"


            jump talk


    label talk:

    scene
    show bg neutral

    show neutral1

    menu:
        "> И что произошло с твои другом?":
            $ points += 1


            show bg love with dissolve

            hide neutral1
            show neutral2

            "'Т-ты заинтересована в этом?..'"

            "'Я не знаю, могу ли говорить об этом...'"

            hide neutral2
            show happ4

            "'Н-но думаю, что могу доверять тебе!.. Посмотрим...'"

            show bg neutral with dissolve
            hide happ4
            show neutral1



            "'У меня было пару друзей в школе, если честно... из этого никогда ничего не выходило.'"


            "'Иногда мы вместе обедали на крыше... Жаловались на учителей.'"

            hide neutral1
            show sad2

            "'Они были хорошими людьми. Но вероятно, они не звали меня своим другом ...'"

            hide sad2
            show sad3

            "'И тогда я встретил Хиёри, и они... просто исчезли.'"


            "'Сначала они прекратили общаться со мной, а потом перевелись в другие школы.'"

            hide sad3
            show sad4

            "'Они никогда не отвечали на мои сообщения...'"

            "'Я думал, что могу считать их друзьями.'"

            "'Видимо, это не было взаимно... Это было ожидаемо...'"

            hide sad4
            show sad5

            "'Может быть, я был слишком скучным или... слишком надоедливым. Может быть и то, и то.'"

            menu:
                "> Это не так. Мне нравится говорить с тобой.":
                    $ points += 1

                    scene
                    show bg neutral
                    show sad5
                    show bg love with dissolve

                    hide sad5
                    show shock1

                    "'П-правда?'"

                    "'Я рад знать это!..'"

                    hide shock1
                    show nerv1

                    "'Даже если я не считаю это правдой... Всё равно приятно слышать это.'"

                    hide nerv1
                    show happ4

                    "'Мне нравится разговарить с тобой тоже!'"

                    "'Я знаю, это звучит не искренее, потому что, мне не остаётся ничего другого, кроме этого, но...'"

                    hide happ4
                    show happ1

                    "'Я не лгу. Спасибо, что выслушала меня.'"

                    show bg neutral with dissolve



                    jump about
                "> Неужели Хиёри сказал тебе это?":

                    $ points -= 1

                    scene
                    show bg neutral
                    show sad5
                    show bg bad with dissolve


                    show shock1

                    "'О ч-чём ты говоришь?..'"

                    hide shock1
                    show sad1

                    "'Хиёри может быть слегка гиперопекающим, и иногда он делает странные вещи, но...'"

                    hide sad1
                    show sad2

                    "'Я не думаю, что он связан с этим как-то...'"

                    "Может быть... им не понравилось, что я нашёл нового друга.'"

                    hide sad2
                    show sad5

                    "'Да... Это всё моя вина...'"

                    show bg neutral with dissolve



                    jump about
        "> Ты знаешь, есть ли тут другие скрытые комнаты?":

            $ points += 0


            show bg neutral with dissolve


            show neutral2

            "'Я... Я не уверен...'"

            "'Тут есть пару скрытых комнат, но ты не сможешь их открыть...'"

            hide neutral2
            show neutral1

            "'Ты смогла зайти в эту комнату, только потому что, Хиёри позволил сделать это.'"

            "Другие комнаты для..."

            hide neutral1
            show sad5

            "'Извини.'"

            "'Я не могу говорить об этом.'"

            "'Я не хочу предасть его.'"

            show bg neutral with dissolve


            jump about
        "> Ты просто хочешь, чтобы я спросила о твоём друге? Ты плохой манипулятор.":

            $ points -= 1

            scene
            show bg neutral
            show neutral1
            show bg bad with dissolve
            hide neutral1

            show shock1

            "'Н-нет!..'"

            hide shock1
            show sad5

            "'Я... Извини, я не хотел, чтобы это звучало так... Ты права.'"

            "'Я не хотел высказываться.'"

            "'У тебя, наверное, итак уже много забот...'"

            hide sad5
            show sad4

            "'Мне жаль. Я знаю, что могут быть надоедливым временами...'"

            "'Или говорить о вещах, которых не должен был...'"

            "'Ты, наверное, не наслаждаешься нашим разговорм с самого начала...'"

            hide sad4
            show sad5

            "'Мне очень жаль.'"

            menu:
                "> Это не так. Я не хотела звучать грубо.":
                    $ points += 0


                    show bg neutral with dissolve
                    hide sad5

                    show sad1

                    "'...Хорошо.'"

                    hide sad1
                    show sad2

                    "'Дай мне знать, если... Если я буду слишком надоедлив, окей?'"

                    "'Я не хочу быть обузой...'"

                    "'Или задержать тебя.'"

                    hide sad2
                    show sad3

                    "'Я просто хочу лучшего для всех...'"

                    show bg neutral with dissolve


                    jump about
                "> Ты не сказал ничего полезного и не знаешь, когда нужно прекратить говорить.":


                    scene
                    show bg bad
                    show sad5
                    hide sad5
                    stop music



                    show shock1

                    "'. . . !'"

                    "'... Мне ж-жаль.'"

                    show bg sad with dissolve
                    hide shock1
                    show sad5


                    "'Я правда извиняюсь за это...'"

                    show bg afraid with dissolve

                    hide sad5
                    show cry1

                    play sound kirekake

                    "'Мне жаль. Я не побеспокою тебя больше.'"

                    hide cry1
                    show bye1 with hpunch


                    "'Я желаю тебе всего наилучшего.'"

                    hide bye1

                    scene bg black
                    with hpunch
                    pause (1.0)

                    scene mon red with dissolve

                    a "> Дружелюбное лицо внезапно поглотил яркий свет."

                    a "> До того, как ты поняла это, весь монитор стал красным, снова."

                    a "> Чтож. Это было ожидаемо."

                    a "> Ты встала с усталым вздохом."

                    scene bg black with dissolve
                    pause (1.0)

                    a "> И тогда... Ты поняла."

                    scene 1111 with dissolve
                    play music heart_beat01 fadein 1

                    a "> Что-то не так."

                    a "> . . ."

                    a "> Ты чувствуешь, как невыносимое напряжение проходит через твоё тело и делает тебя совершенно неподвижной."

                    a "> Кто-то есть... в этой комнате."

                    a "> Ты не слышишь шагов или дыхания, но ощущаешь это."

                    a "> Ты чувствуешь тяжёлый взгляд на своём затылке."

                    a "> . . . !"

                    play sound earth3

                    scene bg black with hpunch
                    pause (2.0)

                    "Концовка 1"

                    return

    label about:


    scene
    show bg neutral

    show hz1

    menu:
        "> Ты говоришь много о других... Может быть, ты расскажешь немного о себе?":
            $ points += 1

            scene
            show bg neutral
            show hz1
            show bg love with dissolve
            hide hz1

            show neutral1

            "'О других...'"

            "'Если честно, у меня нет других тем для разговора...'"

            "'Да и знакомых много не было...'"

            hide neutral1
            show sad2

            "'О себе... Ох, что я могу рассказать о себе?'"

            show bg neutral with dissolve

            show neutral2


            "'Я довольно скучная личность... Ничего особенного во мне нет.'"

            "'Я просто обычный джоб-хоппер.'"

            "'Большую часть времени я работал в продуктовых магазинах... Ничего особенного.'"

            hide neutral2
            show happ3

            "'Что ты хочешь узнать? У меня не так много полезной информации для тебя, если честно...'"


            menu:
                "> Всё насчёт тебя интересно и полезно. Что ты обычно делаешь здесь, к примеру?":
                    $ points += 1

                    scene
                    show bg neutral
                    show happ3
                    show bg love with dissolve
                    hide happ3

                    show shock1

                    "'. . !'"

                    "'О-ох, Я...'"

                    hide shock1
                    show nerv1

                    "'Я даже не знаю с чего начать!..'"

                    "'П-потому что, с нечего даже начать...'"

                    hide nerv1
                    show neutral2

                    "'Обычно, я просто... Жду, когда Хиёри вернётся...'"

                    "'Но он против того, чтобы я разговаривал с другими...'"

                    hide neutral2
                    show happ1

                    "'Но Мэйпл очень милая. Она всегда спрашивает, не хотел бы я чая и... хаха...'"

                    hide happ1
                    show nerv1

                    "'Я не могу пить, конечно же. Но я бы очень хотел.'"

                    hide nerv1
                    show neutral1

                    "'Кроме этого... Здесь нечего делать...'"

                    "'. . .'"

                    hide neutral1
                    show happ2

                    "'Но я действительно рад, что ты спросила меня...'"

                    show bg neutral with dissolve
                    hide neutral1
                    show happ2

                    "'Хиёри так же спрашивал меня, насчёт моих интересов и многом другом, и так далее... Так или иначе, я правда не понимаю почему.'"

                    hide happ2
                    show neutral2

                    "'Он знает уже всё.'"

                    "'Но я не могу сказать 'нет',когда он просит рассказать всё это снова...'"

                    hide neutral2
                    show sad1

                    "'. . .'"

                    hide sad1
                    show nerv1

                    "'И-извини!... Я снова говорю о нём...за его спиной...'"

                    "'Это не очень хорошо с моей стороеы.'"



                    jump notsorry
                "> Я передумала. Давай поговорим о чём-нибудь ещё. Расскажи мне больше о Хиёри?":


                    label hiyori:

                    $ points -= 1

                    scene
                    show bg neutral
                    show happ3
                    show bg bad with dissolve
                    hide happ3


                    show sad1

                    "'. . .'"

                    hide sad1
                    show sad2

                    "...Понятно..."

                    "Хиёри он... очень своебразный.'"

                    hide sad2
                    show nerv1

                    "'Он мой лучший друг, но всё же... Я имею в виду, у всех есть свои странности, верно?'"

                    hide nerv1
                    show neutral1

                    "'Но, несмотря на это, он... очень очень умный.'"

                    "'У него куча друзей. Он не как я...'"

                    hide neutral1
                    show sad2

                    "'Я могу только желать, быть более похожим на него... Только без этих жутких частей.'"

                    "'Неудевительно, почему ты хочешь узнать о нём побольше...'"

                    hide sad2
                    show sad1

                    "'. . .'"

                    hide sad1
                    show nerv1

                    "'П-просто... Будт более осторожна, хорошо?..'"

                    "'Иногда я... Не ощущаю себя в безопасности рядом с ним...'"

                    "'Не то чтобы он делал что-то странное или плохое со мной, просто...'"

                    show bg neutral with dissolve
                    hide nerv1
                    show neutral1

                    "'Как я сказал ранее, он очень своебразный...'"

                    "Может быть, это из-за его... взгляда?'"

                    hide neutral1
                    show sad1

                    "'...Ох...'"

                    hide sad1
                    show nerv1

                    "'Это ужасно говорить за спиной своих друзей. Мне очень жаль.'"



                    jump notsorry
        "> Ты можешь рассказать немного больше о Хиёри? Я хочу знать больше, он выглядит интереснее тебя.":



            jump hiyori
    label notsorry:

    scene
    show bg neutral
    show neutral2

    menu:
        "> Ты немного напряжён. Могу ли я что-то сделать для тебя?":
            $ points += 1

            scene
            show bg neutral
            show neutral2
            show bg love with dissolve
            hide neutral2

            show shock1

            "'... Н-напряжён?'"

            hide shock1
            show nerv1

            "'Н-не совсем, я просто... много заикаюсь.'"

            "'Я думаю, это всегда было у меня...'"

            hide nerv1
            show happ1

            "'Поверь, я наслаждаюсь твоей компанией!'"


            "'Я ощущаю себя легче, когда разговариваю с тобой... Правда!'"

            hide happ1
            show happ3

            "'. . .'"

            show bg neutral with dissolve
            hide happ3
            show hz1


            "'Я знаю, что тебе придёться уйти, рано или поздно...'"

            hide hz1
            show sad1

            "'Всем приходилось...'"

            ". . ."

            hide sad1
            show happ4

            "'Но если мы когда-нибудь ещё раз встретимся... Я был бы очень рад!..'"

            show bg neutral with dissolve

            jump touch
        "> Тебе не нужно так много извиняться. Я тебя не осуждаю. В конце концов, мы друзья.":

            $ points += 0

            scene
            show bg neutral
            show neutral2
            show bg bad with dissolve
            stop music
            hide neutral2

            show scared1

            "'. . .'"

            hide scared1
            show scared2

            "'Д... Друзья?..'"

            "'... Д-да, наверное мы...'"

            "'Я... Мне ж-...'"

            hide scared2
            show nerv1

            "'Я почти сказал это снова... Хаха...'"

            "'Но... Ты правда видишь во мне друга?'"

            show bg neutral with dissolve

            show nerv1
            play music denpa fadein 1

            "'Я... Никто не звал меня так очень давно...'"

            hide nerv1
            show sad1

            "'То есть, я почти знаю тебя!..'"


            "'Но всё же...'"

            hide sad1
            show happ3

            "'Я рад, что у меня появилась возможность поговорить с кем-то...'"

            hide happ3
            show sad2

            "'С кем-то другим...'"


            jump touch
        "> Я не совсем понимаю, как работаю ИИ. Ты не должен быть таким напряжённым.":

            $ points -= 1

            scene
            show bg neutral
            show neutral2
            show bg bad with dissolve
            hide neutral2

            show sad1

            "'Это... не так...'"

            "'Я могу чувствовать...'"

            hide sad1
            show sad2

            "'Я... Я могу испытывать страх, так же как и ты... И я так же запутан, как и ты...'"

            "'Даже если я всего лишь код...'"

            hide sad2
            show sad5

            "'Я до сих пор боюсь исчезнуть.'"

            "'Я боюсь стать бесполезным... навязчивым... никчёмным...'"

            "'Потому что, тогда меня точно удалят.'"

            hide sad5
            show sad4

            "'Как старые игры, от которых ты устал.'"

            "'. . .'"

            hide sad4
            show sad5

            "'Ты можешь легко разбить экран...'"

            "'. . .'"
            show bg sad with dissolve


            show scared1

            "'. . .'"

            hide scared1
            show scared2

            "'Т-ты же не станешь этого делать, в-верно?..'"

            menu:
                "> Конечно нет. Я бы забрала тебя и твой монитор, если бы могла.":
                    $ points += 1

                    scene
                    show bg sad
                    show scared2
                    show bg love with dissolve
                    hide scared2


                    show shock1

                    "! . ."

                    hide shock1
                    show nerv1

                    "'Хаха... Я... Я не думаю, что это так легко...'"

                    "'Монитор, наверное, очень тяжёлый... Хаха...'"

                    hide nerv1
                    show sad1

                    "'Кроме того... Я не думаю, что...смогу уйти вообще.'"

                    "'Я не хочу никаких проблем...'"
                    show bg neutral with dissolve


                    jump touch
                "> Даже если бы я захотела, это было бы слишком опасно. Кто-то хочет, чтобы бы ты остался здесь.":

                    $ points -= 1

                    scene
                    show bg sad
                    show scared2
                    show bg bad with dissolve
                    hide scared2


                    show sad2

                    "'Ох...'"

                    "'Точно...'"

                    hide sad2
                    show sad5

                    "'. . .'"

                    "'Я... Я обещаю, что не хочу навредить тебе, правда...'"

                    "'Но... Я могу понять, почему ты мне не доверяешь. Прости.'"
                    show bg neutral with dissolve


                    jump touch
                "> Даже если я уничтожу тебя, то, у тебя есть резервный файл или типо того. Это бессмыслено.":

                    $ points -= 1

                    scene
                    show bg sad
                    show bg bad with dissolve


                    show scared1

                    "'! . .'"

                    "'Это... Это не совсем там...'"


                    show sad4

                    "'Прямо сейчас... У меня нет никаких копий себя...'"

                    "'Если ты сломаешь экран, я не... восстановлюсь...'"

                    "'. . .'"

                    show bg sad with dissolve


                    show scared1

                    "'П-почему ты так смотришь на меня?..'"
                    show bg neutral with dissolve


                    jump touch


    label touch:

    scene
    show bg neutral

    show sad1

    "'Ты знаешь... Я не говорил с кем-то так много уже очень давно...'"

    hide sad1
    show neutral2

    "'То есть, Хиёри - прекрасный слушатель, но...'"

    hide neutral2
    show sad2

    "'Это словно... Он вообще не участвует в разговоре...'"

    "'Но недавно он обновил мой монитор, чтобы у меня был сенсорный экран, и теперь...'"

    hide sad2
    show nerv1

    "'Всё что он делает, так тычет моё лицо...'"

    "'Это... немного раздражает!..'"

    a "> Он смотрит на тебя так, словно чего-то ожидает..."

    a "> ...Он не очень хорош в манипуляции."

    a "> Ты не уверена, может ли ИИ, что- то чувствовать, но ты решила всё же попробовать."

    menu:
        "> Погладить его по голове":

            scene
            show bg neutral
            show bg love with dissolve
            show pat3 with dissolve

            "'! . .'"

            "'. . .'"

            "'. . .'"

            "'Он... Он никогда не делал такое раньше...'"

            "'Это странно... но ощущается приятно...'"

            hide pat3
            show happ2 with dissolve

            "'...Спасибо...'"

            "'Обычно, он просто дергает мои щёки...'"

            show bg neutral with dissolve


            jump hobby
        "> Тыкнуть его нос":


            scene
            show bg neutral
            show bg love with dissolve
            show pat2 with dissolve
            play sound cat_like1a

            "'! . .'"

            "'. . .'"

            "'О-окей...'"

            "'Я не могу чувствовать, как теплы твои руки, но...'"

            hide pat2
            show hz1 with dissolve

            "'Это немного странно...'"

            show bg neutral with dissolve

            jump hobby
        "> Ущипнуть его за щёку":


            scene
            show bg neutral
            show bg bad with dissolve


            show pat1 with dissolve
            play sound squeaky_toy

            "'Ау!..'"

            "'. . .'"

            "'...Пожалуйста, хватит..."

            "'. . .'"


            show sad1 with dissolve
            hide pat1

            "'Хиёри всегда делает так...'"

            "'Это не так больно, но всё же...'"

            "'Это неприятно.'"

            show bg neutral with dissolve

            jump hobby



    label hobby:

    scene
    show bg neutral
    show nerv1

    "'Ох!...'"

    "'Я думаю, что... говорю только о себе...'"

    "'Это немного смущает, хаха...'"

    hide nerv1
    show neutral2

    "'Извини, что не спросил раньше, но...'"

    "'Я пойму, если ты не захочешь делиться...'"

    "'Но ты можешь немного рассказать о себе?'"

    hide neutral2
    show neutral1

    "'К примеру, я... Эм...'"

    hide neutral1
    show happ3

    "'Я люблю видеоигры!..'"

    hide happ3
    show happ1

    "'Особенно с мультиплеером...'"

    "'Если бы можно было установить парочку игр здесь...'"

    hide happ1
    show happ4

    "'Я был бы счастлив поиграть с тобой!..'"

    hide happ4
    show nerv1

    "'Если ты не против, конечно!'"

    "'Это было бы очень круто...'"

    hide nerv1
    show neutral1

    "'У тебя есть хобби? Что ты любишь делать в свободное время?'"

    python:
        povhobby = renpy.input("Что ты любишь делать в свободное время?", length=32)
        povhobby = povhobby.strip()

    if povhobby in ["art", "ART", "Art", "drawing", "Drawing", "DRAWING", "making art", "Making art", "making Art", "Making Art"]:
        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1

        show happ1

        "'Drawing!...'"

        hide happ1
        show happ4

        "'That's so nice!.. It's wonderful that you have a thing that you enjoy doing...'"

        hide happ4
        show neutral1

        "'To be honest, I've never talked to any artists...'"

        "'So I don't really know much about it and what to say...'"

        "'But one thing for sure...'"

        hide neutral1
        show happ2

        "'Don't forget to take a break from time to time, okay?..'"

        "'Don't overwork yourself and your hand, and leave some time for yourself to relax.'"



        label goodboy:

            scene
            show bg love

            show neutral2

            "'Sometimes the inspiration comes in sudden bursts...'"

            "'But you and your wellbeing should always be your number one priority!...'"

            hide neutral2
            show happ3


            "'It's easier to do your favorite things when you're well rested.'"

            "'And even if you don't like what you can do right now...'"

            hide happ3
            show happ5
            play sound cat_like1a

            "'There are people who love what you do!'"

            "'And who love YOU, too!'"

            hide happ5
            show neutral2

            "'You can say a lot about a person by looking at their work!..'"

            hide neutral2
            show happ3

            "'I might not be very knowlegable, but I wish you only the best in your endevours!..'"

            "'Just remember that your hobby is something you do for yourself, and not for somebody else.'"

            hide happ3
            show happ1

            "'Then it will bring you much more enjoyment.'"

            hide happ1
            show nerv1

            "'I-I'm sorry, I got a bit carried away!.. I'd be happy if you've ever shown your work to me, haha...'"

            hide nerv1
            show happ4

            "'Thank you for sharing with me!'"

            show bg neutral with dissolve


            jump final

    elif povhobby in ["photo", "Photo", "PHOTO", "photography", "Photography", "PHOTOGRAPHY", "taking photos", "Taking photos", "Taking Photos", "photos", "PHOTOS", "Photos"]:

        scene
        show bg neutral
        show neutral1
        show bg bad with dissolve
        hide neutral1



        show scared1

        stop music
        play sound accent401

        "'. . . !'"

        hide scared1
        show scared2

        "'You... like t-taking photos?..'"

        hide scared2
        show nerv1

        "'Haha... It's... a nice hobby!..'"

        "'Yeah...'"

        hide nerv1
        show scared1

        "'. . .'"

        hide scared1
        show nerv1

        "'It's... very creative...'"

        "'. . .'"


        show bg neutral with dissolve
        show sad2
        play music denpa fadein 1

        "'Hiyori-kun... also enjoys photography.'"

        "'I don't really understand it...'"

        hide sad2
        show nerv1

        "'I-I mean!.. The landscape photos he takes are very pretty but...'"

        "'. . .'"

        hide nerv1
        show sad1

        "'I'm sorry for my reaction.'"

        hide sad1
        show neutral1

        "'I don't know what kind of photos you like to take... Portraits, landscapes, but...'"




        jump goodboy

    elif povhobby in ["sport", "Sport", "SPORT", "Sports", "SPORTS", "sports", "playing sports", "Playing sports", "football", "Football", "Basketball", "basketball", "baseball", "Baseball", "soccer", "Soccer", "gymnastics", "Gymnastics", "swimming", "Swimming"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1

        show happ1

        "'You like sports? That's so cool!'"

        "'I envy you, haha...'"

        hide happ1
        show happ4

        "'I've been on a weaker side since I remember...'"

        hide happ4
        show nerv1
        play sound powerdown07

        "'I can't imagine being able to train regularly, to be honest...'"

        hide nerv1
        show happ2

        "'But if you really enjoy it, it's very nice!'"

        "'I would gladly watch you practice...'"

        hide happ2
        show happ1

        "'. . .'"

        "'M-maybe you could train me... Haha...'"

        "'It would be fun!..'"

        hide happ1
        show happ3

        "'Right now I'm not bad at swiming!..'"

        "'So, if we ever met again, we could come up with something!'"

        "'I'd be more than happy to train with you!'"

        hide happ3
        show nerv1

        "'I-I realize that it sounds absurd, haha...'"

        hide nerv
        show happ4

        "'Thank you so much for sharing with me!'"

        show bg neutral with dissolve



        jump final

    elif povhobby in ["writing", "Writing", "WRITING", "to write", "write", "Write", "Fic writing", "fic writing", "ficwriting", "Ficwriting", "writing fics", "Writing fics", "poetry", "Poetry", "writing poetry", "Writing poetry"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show neutral2

        "'O-oh, you're a writer?'"

        hide neutral2
        show happ1

        "'That's so cool!..'"

        "'You know, you could say I am a writer too, in a sense!'"

        hide happ1
        show happ4

        "'I really like coding...'"

        "'I'm not very good at it yet, but... I'm improving every day!'"

        hide happ4
        show neutral2

        "'Besides, I have an access to any educational info on this computer...'"

        "'You're probably writing something more... poetic?'"

        hide neutral2
        show happ3

        "'It would be nice to read one of your works sometime!..'"



        jump goodboy

    elif povhobby in ["gaming", "Gaming", "games", "Games", "playing games", "Playing games", "video games", "Video games"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show shock1

        "'. . !'"

        "'I-I love it too!'"

        hide shock1
        show happ1

        "'Ah, I must've told you about it before already...'"

        "'But I also love gaming!'"

        hide happ1
        show happ3

        "'Sometimes I like to play something hardcore...'"

        "'But to be honest, most of all I enjoy sandbox games.'"

        "'You can just sit and relax after a hard day...'"

        "'Just run around and look at pretty landscapes... Farm games are also very relaxing...'"

        hide happ3
        show happ2

        "'Can you tell me about your favorite games when we meet again?'"

        hide happ2
        show happ1

        "'If we get the opportunity, of course...'"

        "'It would be very nice!'"

        hide happ1
        show happ3

        "'Just don't forget to take breaks while playing... Your eyes can get tired pretty quickly, even if your brain is relaxing.'"

        "'Thank you so much for sharing with me!'"



        jump final

    elif povhobby in ["music", "Music", "playing music", "Playing music", "playing instruments", "Playing instruments", "playing piano", "Playing piano", "playing guitar", "Playing guitar", "piano", "Piano", "Guitar", "guitar"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show neutral2

        "'O-oh, you play music?'"

        hide neutral2
        show happ4

        "'That's so cool!..'"

        "'I never understood how to write music...'"

        hide happ4
        show neutral1

        "'I think, Hiyori-kun mentioned that he can play a couple of instruments... He can play piano for sure...'"

        hide neutral1
        show nerv1

        "'Ah!... I'm sorry, didn't mean to talk about him again.'"

        hide nerv1
        show happ1

        "'Anyways... I tried playing piano once, and never touched it again.'"

        "'But I enjoy listening to music!..'"

        "'Being able to create something is so amazing...'"



        jump goodboy

    elif povhobby in ["nothing", "Nothing", "NOTHING"]:

        scene
        show bg neutral
        stop music
        show neutral1
        show bg bad with dissolve
        hide neutral1

        show sad1



        "'. . .'"

        hide sad1
        show sad2

        "'O-okay...'"

        "'I don't mind if you don't want to share...'"

        hide sad2
        show happ3

        "'Just know that whatever it is, I support you and your hobby, and I'm glad you have a thing you enjoy doing!'"

        "'A hobby helps you forget about the world when everything is... too much.'"

        hide happ3
        show nerv1

        "'Sorry, that sounded grim.'"

        hide nerv1
        show sad2

        "'. . .'"

        hide sad2
        show neutral1
        play music denpa fadein 1

        "'But you know... It would be nice if we got an apportunity to talk about it sometime.'"

        "'But I can understand your distrust.'"
        show bg neutral with dissolve

        jump final

    elif povhobby in ["срать", "СРАТЬ", "Срать", "какать", "Какать", "КАКАТЬ", "srat", "SRAT", "Srat", "srat'", "SRAT'", "Srat'"]:

        scene
        show bg neutral
        show neutral1
        show bg black with dissolve
        hide neutral1

        show nerv1

        "'. . .'"

        "'Я же просил, давай без этого...'"

        "'А как же обещание... Сделать вид, что ничего не было...'"

        hide nerv1
        show hz1

        "'Кхм.'"

        hide hz1
        show happ3

        "'Очень классное хобби.'"

        "'Довольно... нестандартное. Для человека.'"

        hide happ3
        show nerv1

        "'Как ты видишь, я... На данный момент просто ПО, поэтому возможность выполнять данную функцию... у меня отсутствует.'"

        "'Но я, эм... Поддерживаю тебя... В твоих начинаниях.'"

        hide nerv1
        show hz1

        "'. . .'"

        hide hz1
        show nerv1

        "'Не обосрись, да не обосран будешь.'"
        show bg neutral with dissolve

        jump final

    elif povhobby in ["скульптуры", "Скульптуры", "скульптурирование", "Скульптурирование", "лепить", "Лепить"]:

        if povname in ["соу", "хиёри", "соу хиёри", "хиёри соу", "Соу", "Хиёри", "Соу Хиёри", "Хиёри Соу"]:

            jump secret
        else:


            scene
            show bg neutral
            show neutral1
            show bg love with dissolve
            hide neutral1


            show neutral2

            "'Скульптуры?..'"

            hide neutral2
            show nerv1

            "'Ахах... Звучит слегка знакомо.'"

            "'Я не знаю об этом слишком много, но я думаю...'"

            hide nerv1
            show happ1

            "'Хиёри однажды рассказывал мне об этом.'"

            "'Он говорил, что наслаждается этим так же, как и фотографией...'"

            hide happ1
            show neutral2

            "'Я не могу даже представить, чтобы делать что-то наподобие такого, заставляя твёрдые объекты выглядеть такими мягкими и живыми...'"

            jump goodboy
    else:


        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show happ2

        "'That's so cool!'"

        "'I'm glad you have something you enjoy doing.'"

        hide happ2
        show happ1

        "'I love seeing how happy people get when they are talking about something they like...'"

        "'Even if I'm not very knowledgeble in this, I hope doing it helps you through the bad times...'"

        "'A hobby helps you forget about the world when everything is... too much.'"

        hide happ1
        show nerv1

        "'Sorry, that sounded grim.'"

        hide nerv1
        show happ2

        "'I'm just glad you have something you enjoy doing.'"

        hide happ2
        show neutral1

        "'But... It would be nice if we got an apportunity to talk more about it sometime.'"

        "'I know, right now is not the best time for that...'"

        hide neutral1
        show happ3

        "'Maybe in future... Haha...'"


        show bg neutral with dissolve

        jump final

    label final:

    scene
    show bg neutral
    show neutral1

    menu:
        "> That's really nice of you. (Pet the monitor)":
            $ points += 1

            scene
            show bg neutral
            show neutral1
            show bg love with dissolve
            hide neutral1
            show pat3 with dissolve
            play sound accent281

            "'! . . .'"

            "'. . .'"

            "'Th-thank you...'"

            hide pat3
            show happ1 with dissolve

            "'I'm glad to hear it!..'"

            "'I-I'm not that nice, but...'"

            hide happ1
            show happ3

            "'I'm just happy to help you...'"

            "'You're a good person. I can see that!'"



            jump finish
        "> Even if you don't know that much about it... Thank you.":

            $ points -= 0

            scene
            show bg neutral
            show neutral1
            show bg neutral with dissolve
            hide neutral1

            show nerv1

            "'Haha, yes... I really don't know much...'"

            "'As I said... I'm an ordinary and boring person, but...'"

            hide nerv1
            show happ3

            "'I'm happy to hear that I could keep you company!..'"

            "'Thank you, too!'"



            jump finish
        "> I don't need your fake support.":

            $ points -= 1

            scene
            show bg neutral
            show neutral1
            show bg bad with dissolve
            hide neutral1

            show shock1

            "'Ah!...'"

            hide shock1
            show sad5

            "'I-I understand your distrust, but...'"

            "'My support... isn't fake...'"

            hide sad5
            show sad4

            "'. . .'"

            "'Sorry if I upset you with my words...'"

            "'I'm not very good at that...'"

            "'I never wanted to make you upset...'"

            jump finish

    label finish:



    if points >= 58:

        show bg love with dissolve
        scene
        show bg love
        show sad1
        play music hakanai fadein 1

        "'I know we don't have much time left but...'"

        hide sad1
        show happ3

        "'I'm glad I got to spend some time with you!'"

        "'It would be nice to meet you again in the future... When things are... normal again.'"

        hide happ3
        show happ1

        "'We could talk more about you, your interests, your hobbies... I would be glad if we...'"

        "'If we...'"

        "'. . .'"

        hide happ1
        show shy1

        "'If we..could become real friends!..'"

        "'I'd love to be able to... call myself your friend...'"

        "'I'm sorry if this is too sudden!..'"

        hide shy1
        show happ1

        "'I'm just a bit nervous but... in a good way!..'"

        "'To be honest, I haven't felt at ease like this for a long time...'"

        hide happ1
        show happ3

        "'Thank you!..'"

        "'You came here even though it's dangerous to walk alone, but... I'm glad I met you.'"

        hide happ3
        show happ1

        "'Even for a little while.'"

        "'If I could ever help you with anything... Don't hesitate to ask!'"

        hide happ1
        show bye2 with dissolve

        "'I wish you only the best... Even if it's not right to say goodbye like that...'"

        "'Maybe next time we could play games together...'"

        "'A fighting game or... a farm?'"

        "'I would be so happy to spend time with you again.'"

        "'And also, we-...'"

        stop music fadeout 2

        "'. . .'"

        "'. . .'"

        hide bye2
        show bg afraid
        show bye3 with hpunch

        "'. . .'"

        "I-I'm sorry, I..."

        "'I'm sorry!'"

        "'You should-!'"

        hide bye3
        play sound computer

        scene bg black
        with hpunch
        pause (1.0)

        scene mon red with dissolve

        a "> The friendly face has been suddenly consumed by the bright light."

        a "> Before you were able to aknowledge it, the whole screen is burning red again."

        a "> What happened?"

        a "> You desperately touch the screen a couple of times, but there's no response."

        scene bg black with dissolve
        pause (1.0)

        a "> And this is when... You understand."

        scene 1111 with dissolve
        play music heart_beat01 fadein 1

        a "> Something's not right."

        a "> . . ."

        a "> You feel an unberable tension going through your body and making you completely still."

        scene end1 with dissolve

        a "> There's someone else... in the room."

        a "> You can't hear the steps nor the breathing, but you feel it."

        a "> You feel a heavy gaze on the back of your head."

        a "> . . ."

        scene bg black with dissolve
        pause (1.0)

        stop music

        m "'Hey there...'"

        m "'Haha... What are you doooing here?'"

        m "'Actually, that's mine...'"

        scene end2
        play sound horror_pianochord3

        m "'Weren't you taught not to stick your nose where it doesn't belong?'"

        m "'You're being awfully nice, aren't you?'"

        m "'It's a good thing I know juuuust how to fix this! Haha...'"

        play sound earth3
        scene bg black with hpunch
        pause (2.0)

        "END 2"

        return

    elif points <= 45:


        show bg sad with dissolve
        scene
        show bg sad
        show sad2
        play music hazama1 fadein 1

        "'I know we don't have much time left but...'"

        hide sad2
        show sad1

        "'I just don't understand... What did I do wrong?..'"

        "'I mean, I wasn't mean to you...'"

        "'Or do you just see me as an enemy because I'm... in this room? And because I know Hiyori-kun?'"

        "'I can understand that but...'"

        hide sad1
        show sad5

        "'. . .'"

        hide sad5
        show cry1

        play sound kirekake

        "'I-I'm sorry, it's just... not fair!..'"

        "'I never wanted to harm you, and...'"


        show bg afraid with dissolve
        hide cry1
        show cry2

        "'I've never tried to do anything to you while we were talking!...'"

        "'Even if I'm not a human, my conscious is... It's still the same as yours, as of any human...'"

        "'. . .'"

        hide cry2
        show bye1 with hpunch

        "'I'm sorry. I won't bother you anymore since you dislike me so much.'"

        hide bye1 with hpunch

        scene bg black
        with hpunch
        pause (1.0)

        scene mon red with dissolve

        a "> The friendly face had been suddenly consumed by the bright light."

        a "> Before you were able to aknowledge it, the whole monitor is burning red again."

        a "> Well. That was expected."

        stop music fadeout 2

        a "> You get up with a tired sigh."

        scene bg black with dissolve
        pause (1.0)

        a "> And this is when... You understand."

        scene 1111 with dissolve
        play music heart_beat01 fadein 1

        a "> Something's not right."

        a "> . . ."

        a "> You feel an unberable tension going through your body and making you completely still."

        a "> There's someone else... in the room."

        a "> You can't hear the steps nor the breathing, but you feel it."

        a "> You feel a heavy gaze on the back of your head."

        a "> . . ."

        scene bg black with dissolve
        pause (1.0)
        stop music

        m "'Hey there...'"

        m "'Haha... What are you doooing here?'"

        m "'Actually, that's mine...'"

        scene 11112
        play sound horror_pianochord3

        m "'Weren't you taught not to stick your nose where it doesn't belong?'"

        m "'So rude of you...'"

        m "'It's a good thing I know juuuust how to fix this! Haha...'"

        play sound earth3
        scene bg black with hpunch
        pause (2.0)

        "END 3"

        return
    else:




        show bg neutral with dissolve
        scene
        show bg neutral
        show sad1
        play music tunagu2 fadein 1


        "'I know we don't have much time left but...'"

        hide sad1
        show neutral2

        "'It was nice to spend time with you.'"

        "'Even if you still don't trust me completely, I can understand why...'"

        hide neutral2
        show happ3

        "'I'd be glad to get to know you more...'"

        "'Haha...'"

        hide happ3
        show neutral1

        "'But if you ever need my help...'"

        "'Don't be afraid to ask.'"

        hide neutral1
        show happ4

        "'Thank you for spending time with me...'"

        hide happ4
        show neutral2

        "'You probably should go back to your friends before it's to late...'"

        "'And don't worry, I won't tell anyone you were here!'"

        hide neutral2
        show happ2

        "'I wish you only the best!..'"

        hide happ2
        play sound computer

        scene bg black with dissolve
        pause (1.0)


        scene mon red with dissolve

        a "> Before you could answer, the screen went red again."

        a "> Well... It was an Experience."

        a "> You didn't learn anything that would help you, but for some reason you feel... at ease."

        a "> Maybe you just needed a distraction."

        scene bg monitor room 1 with dissolve
        play music tansaku3 fadein 1

        a "> You get up from your chair with a sigh and walk to the door."

        a "> You hear steps from behind it."

        a "> Feeling determined, you open the door."

        scene bg black with dissolve
        pause (2.0)

        "END 4"
        stop music fadeout 2

        return






    return





label secret:



    scene
    show bg neutral
    show neutral1
    show bg love with dissolve
    hide neutral1


    show neutral2

    "'Скульптуры?..'"

                hide neutral2
                show nerv1

                "'Ахах... Звучит слегка знакомо.'"

                "'Я не знаю об этом слишком много, но я думаю...'"

                hide nerv1
                show happ1

                "'Хиёри однажды рассказывал мне об этом.'"

                "'Он говорил, что наслаждается этим так же, как и фотографией...'"

                hide happ1
                show neutral2

                "'Я не могу даже представить, какого это делать что-то наподобие такого, заставляя твёрдые объекты выглядеть такими мягкими и живыми...'"

    hide neutral2
    show hz1
    pause (1.0)

    stop music fadeout 2

    a "> Что-то не так."

    a "> Ты не знаешь почему, но по какой-то причине каждое его слово вызывает у тебя все большую и большую тошноту."

    a "> Твои руки становятся холодными и дрожащими."

    a "> Но ты не можешь собраться и сказать ему остановится."

    hide hz1
    show happ1

    "'Ох!.. Я вспомнил, что он показывал мне пару своих работ...'"

    "'Они были не закончены, но... Они всё равно выглядели довольно круто!'"

    hide happ1
    show hz1

    "'. . .'"

    play music heart_beat01 fadein 2

    "'. . .'"

    hide hz1
    show nerv1

    "'Хэй...'"

    "'Ты в порядке?'"

    "'Ты выглядишь бледной...'"

    a "> Это было бы странно, если бы ты не была бледной в такой ситуации."

    a "> Что-то в его словах заставило тебя бояться."

    a "> Твои руки сжались в кулаки, когда ты с тревогой оглядела комнату."

    a "> Ты не можешь издать и звука. Ты слишком занята, отчаянно хватая ртом воздух."

    scene
    show bg love
    show nerv1
    show bg afraid with dissolve
    hide nerv1

    show scared1

    "'Х-хэй!..'"

    "'Я не... Где-то здесь должна быть бутылка воды позади тебя, пожалуйста, возьми её!..'"

    hide scared1
    show scared2 with hpunch

    "'Пожалуйста, оста-...'"

    scene bg black with dissolve
    stop music fadeout 2

    a "> Его голос становится далеким, пока не растворяется в пустоте."

    a "> И затем... темнота полностью охватывает тебя."

    window hide dissolve

    pause(3.0)

    pov "'. . .'"

    pov "'. . .'"

    pov "'. . .'"

    pov "'. . ?'"

    w "'Хэй...'"

    w "'Шин...'"

    w "'Вставай.'"

    b "'Что...'"

    scene shinsleep with dissolve
    pause(2.0)

    scene shinwake with dissolve
    pause(1.0)

    b "'Хмм...'"

    pov "Ты открыл свои глаза, но потом сразу же зажмурился. Из-за яркого света твоя голова разболелась как в аду."

    b "'Агх...'"

    w "'Давай... Ты не можешь спать весь день.'"

    pov "Ты был... сонным?"

    pov "Постепенно, ты начинаешь осознавать, где находишься."

    play music hazama2 fadein 3

    scene souroom with dissolve
    pause(1.0)

    pov "Конечно, ты не дома. Но это место уже стало твоим вторым домом."

    pov "Необъяснимая тревога наполняет тебя, страно смешиваясь с содержащим, и это заставляет тебя полностью проснуться."

    pov "Уже вечер?"

    b "'Агх... Моя спина болит...'"

    show sou4 with dissolve

    c "'Конечно она будет. Я ушёл на пару минут, чтобы взять кружку кофе, а ты уже удобно разлёгся на столе.'"

    c "'Ты мог бы занять диван, знаешь... Это плохо для твоей спины!'"

    hide sou4
    show sou3

    c "'Ты мог бы свалиться со стула или монитор мог упасть тебе на голову. Он довольно тяжёлый.'"

    pov "Ты никогда не думал об этм раньше, но теперь видимо будешь."

    pov "Ты не мог вспомнить, когда заснул, но это больше не беспокоило тебя."

    show sou3 at right with move

    show shin3 at left with dissolve

    b "'Аха, да... Это могло...'"

    hide shin3
    show shin4 at left

    b "'Т-ты не возражаешь, если я вздремну ещё раз? Я не очень хорошо себя чувствую...'"

    hide sou3
    show sou1 at right

    c "'Я не против, но ты уверен, что почувствуешь себя лучше?'"

    c "'Ты итак проспал большую часть дня. Твоя голова наверное болит очень сильно. Поверь мне, я знаю какого это.'"

    hide shin4
    show shin1 at left


    b "'Мм... Может быть ты прав... Моя голова итак уже сильно болит...'"

    pov "Он всегда прав."

    hide sou1
    show sou12 at right

    c "'Ох, я могу помочь тебе окончательно проснуться!'"

    c "'Ты пообещал, что поможешь мне. Итак...'"

    hide sou12
    show sou11 at right

    c "'Ты помнишь игру, которую я тебе показывал?'"

    hide shin1
    show shin6 at left

    b "'Какую из?..'"

    hide sou11
    show sou14 at right

    play sound extend1

    c "'Хаха, твоя память уже начинает ухудшаться? Это не очень хороший знак, для твоего возраста.'"

    hide sou14
    show sou12 at right

    c "'Хорошо, что у тебя есть я! Не нужно тратить кучу денег на доктора, когда у тебя есть эти игры.'"

    hide shin6
    show shin5 at left

    b "'. . .'"

    b "'Ты имеешь в виду, карточную игру?'"

    hide sou12
    show sou5 at right

    c "'Бинго! Ты можешь запомнить всё что угодно, если просто постараешься. Видишь? Мои методы уже работают!'"

    c "'Теперь, посмотри на монитор.'"

    stop music fadeout 2

    scene screen1 with dissolve
    pause(1.0)

    play sound computer

    scene screen2 with hpunch
    pause(0.5)

    play music nounai fadein 2

    c "'Итак, давай начнём с простого. Твой мозг,должно быть, полон паутиной! Ты вообще помнишь, о чём эта игра?'"

    b "'Ухх... Это похоже на игру в'Оборотня' или 'Мафию', верно?'"

    show screen4

    c "'Хаха, почти. Прошло много времени с тех пор, как мы играли в эту игру, не так ли?'"

    play sound powerdown07

    b "'Потому что в это невозможно играть только вдвоём...'"

    c "'Точно. Но это не имеет значения, Шин.'"

    hide screen4
    show screen2

    c "'Смысл этой игры, убедиться, что никто не знает, какая карта у тебя. Даже если осталось всего лишь два человека.'"

    b "'Осталось?..'"

    c "'Ну, кто-то проиграет, если остальные узнают, какая у него карта.'"

    c "'И в какой то момент, эта игра становится один на один. Я думал, ты это уже понял'"

    b "'Точно... И-извини, я, наверное, все ещё сонный.'"

    hide screen2
    show screen4

    c "'Я вижу. Вот поэтому, я всё это напоминаю тебе.'"

    c "'Иногда правила могут быть фальшивыми, как и сами карты. Вот почему ты должен хранить верную информацию в своей голове.'"

    b "'Аха... Разве это не слишком много для простой карточной игры?'"

    c "'Ты хочешь сказать, что не можешь запомнить дажу основу?'"

    c "'Неудивительно, почему ты никогда не можешь выйграть у меня.'"

    b "'Ух... Извини.'"

    hide screen4
    show screen2

    c "'Давай тогда, перейдём к этому.'"

    show card1 zorder 1 with dissolve
    pause(2.0)

    c "'Начнём с простого. Ты помнишь, какая карта является верной?'"

    label firstq:

        menu:
            "Та, что слева":

                b "'Та, что слева?..'"

                label wrong1:

                    hide screen2
                    show screen5
                    show card1 zorder 1

                    play sound buzzer1

                    c "'Как я и думал... Ты знаешь, ассоциативное обучение - один из самых простых способов обучения. Жаль, что это не работает для тебя.'"

                    b "(Чёрт...Это было неверно.)"

                    c "'Правильный, тот что справа. Одна книга, которая закрыта. Видишь, это легко запомнить, ведь так?'"

                    hide screen5
                    show screen2


                    c "'Надеюсь, ты не разочаруешь меня в следующий раз.'"

                    jump secondq
            "Та, что посередине":


                b "'Та, что посередине?..'"

                jump wrong1
            "Та, что справа":


                $ quiz_score += 1
                b "'Та, что справа?..'"

                hide screen2
                show screen4
                show card1 zorder 1

                play sound accent281

                c "'Видишь, ты сделал это! Карта с одной книгой, которая закрыта.'"

                c "'Хорошая работа.'"

                b "'Я-я думаю... Это не было так сложно.'"

                c "'Эти знания однажды могут пригодиться в один прекрасный день! Мы можем когда-нибудь пойти на вечеринку, и в эту игру лучше всего играть с большим количеством людей.'"

                hide screen4
                show screen2

                pov "Ты не уверен, сможешь ли когда-нибудь пойти на вечеринку, но ты всё равно киваешь с неуверенной улыбкой."

                jump secondq

    label secondq:

        c "'Хм..Что бы мне спросить у тебя следующим...'"

        hide card1 with dissolve

        c "'Ох, ты помнишь, какая карта является более значимой в игре?'"

        show card2 zorder 1 with dissolve
        pause(2.0)

        menu:
            "Та, что слева":

                b "'Эм..Слева?'"

                hide screen2
                show screen4
                show card2 zorder 1

                play sound buzzer1

                c "'Хм... жалко, но нет. Это неправильный ответ.'"

                c "'Та, карта с ключом - самая сильная и значимая карта в игре.'"

                c "'Ты должен всегда помнить об этой карте, Шин. Думай об этом так, словно это ваш ключ к победе, хаха!'"

                c "'Это единственная карта, которая может быть раскрыта. Ведь, если она есть у тебя, то остальные игроки не смогут выкинуть тебя, ведь, это значит проигрыш для всех остальных.'"

                hide screen4
                show screen5

                c "'Дело лишь в том... Поверять ли они тебе на слово? Хаха.'"

                b "(Чёрт... Это было неверно.)"

                hide screen5
                show screen2

                c "'Какая жалость. Я надеялся, что ты всё это помните.'"

                jump thirdq
            "Тот, что справа":


                $ quiz_score += 1
                b "'Справа?..'"

                hide screen2
                show screen4
                show card2 zorder 1

                play sound accent281

                c "'Правильно! Ох, ты заставляешь меня чувствовать таким гордым!'"

                b "'Ух... Если я правильно помню, эта карта гарантирует, что тебя никто не тронет. Потому что, если они выберут тебя в качестве виновника, то это мгновенный проигрыш для всех.'"

                b "'Ты всегда должен сообщать людям, что у тебя есть эта карта, верно?'"

                c "'Отличная работа! Ты прав. Ты слушал мои объяснения, в конце концов!'"

                b "'Я всегда слушаю тебя, Хиёри...'"

                hide screen4
                show screen2

                jump thirdq


    label thirdq:

        hide card2 with dissolve

        c "'Итак, что будет следующее.'"

        show eye zorder 1
        pause(0.1)
        hide eye

        show arm zorder 1
        pause(0.1)
        hide arm

        stop music fadeout 1

        show card3 zorder 1 with dissolve
        pause(2.0)

        play sound horror_pianochord3

        b "'! . .'"

        hide screen2
        show screen5

        c "'Мм? Что-то не так?'"

        b "'. . .'"

        b "'Н-нет, просто... ничего.'"

        play music nounai fadein 2

        c "'Ох, хорошо.'"

        hide screen5
        show screen2

        c "'Ты помнишь, какая карта используется в игре?'"

        menu:
            "Та, что слева":

                $ quiz_score += 1
                b "'Та, что слева... Правой не существует, так?'"

                hide screen2
                show screen4

                play sound accent281

                c "'И это правильно! Хаха, хорошая работа, ты не попал в мою ловушку.'"

                c "'Некоторые игровые мастера, могут попытаться обмануть вас и дать вам фальшивую карту. Поэтому ты должен помнить, как выглядят настоящие карты.'"

                c "'Если ты будешь держать эти правила в своей голове, то выйграешь.'"

                c "'Но ты милашка, поэтому можешь не беспокоиться об этом. Никто не захочет избавиться от тебя, если ты посмотришь на них своими большими грустными глазами.'"

                hide screen4
                show screen5

                c "'Люди склонны доверять тем, кто дружелюбен и слаб. Но как долго это продлится? Хаха.'"

                b "'Х-Хиёри!.. Перестань издеваться надо мной...'"

                c "'Ох, я едва шучу!'"

                hide screen5

                jump fourthq
            "Та, что справа":


                b "'Эм... Справа?'"

                hide screen2
                show screen5

                play sound buzzer1

                c "'Хм... Нет, ты ошибься. Ты хотя бы немного слушал мои объяснения?'"

                c "'Эта карта не существует.'"

                c "'Некоторые игровые мастера, могут попытаться обмануть вас и дать вам фальшивую карту. Поэтому ты должен помнить, как выглядят настоящие карты.'"

                hide screen5
                show screen2

                c "'Я надеюсь, ты запомнишь это.'"

                b "(Чёрт... Я ошибся.)"

                hide screen2

                jump fourthq
            "...Что это за картинки были?":


                b "'Х-хиёри...Что это было..?'"

                c "'Что ты имеешь в виду?'"

                b "'Здесь были картинки, которые промелькнули на секунду... Картинки чего..?'"

                hide screen2
                show screen5

                play sound extend1

                c "'Ты пытаешься избежать моего вопроса? Хаха, это так похоже на тебя.'"

                b "'. . .'"

                pov "Ты не можешь избавиться от тревоги."

                pov "Но... Может быть, это просто твоё воображение."

                hide screen5
                show screen2

                c "'Правильная карта, та, что слева. Присмотрись внимательнее.'"

                c "'Некоторые игровые мастера, могут попытаться обмануть вас и дать вам фальшивую карту. Поэтому ты должен помнить, как выглядят настоящие карты.'"

                hide screen2

                jump fourthq

    label fourthq:

        show screen2
        hide card3 with dissolve

        c "'Итак, последний вопрос.'"

        show card4 zorder 1 with dissolve
        pause(1.0)

        c "'Теперь, когда мы знаем, какие карты настоящие... Ты помнишь, как называется эта?'"

        python:
            cardname = renpy.input("Как называется эта карта?", length=32)
            cardname = cardname.strip()

        if cardname in ["ЖЕРТВА", "жертва", "Жертва"]:

            $ quiz_score += 1
            b "Это [cardname], так?"

            hide screen2
            show screen4

            play sound accent281

            c "'Бинго!'"

            c "'Видишь? Это было не так сложно, не так ли? Ты помнишь, что она делает?'"

            b "'Из того, что ты объяснил, это... она почти так же важна, как и ключник? Это одна из самых сильных карт, но... Тебе нужно, чтобы все доверяли тебе. Если они не могут, то это потеря для тебя...'"

            hide screen4
            show screen5

            c "'Ох, ты сегодня просто убиваешь, Шин!'"

            c "'Просто не забывай, что никто не должен знать, что у тебя эта карта. Если она называется ''Жертва'', то ты действительно должен заставить всех поверить, что они должны пожертвовать тобой.'"

            c "'В другом случае, считай, что это проигрыш в тот момент, когда возьмёшь эту карту, хаха.'"

            b "'Ты когда-нибудь выйгрывал с этой картой?'"

            hide screen5
            show screen4

            c "'Хм? Почему ты спрашиваешь?'"

            b "'Ну... Ты играл в эту игру ранее, и ты знаешь правила очень хорошо... Тебе удавалось выйгрывать с этим раньше?'"

            c "'Может быть. Оставлю это твоему воображению.'"

            b "'Хиёри!.. Я сделал всё возможное, чтобы ответить на твой вопрос, так почему, ты не можешь ответить на мой?..'"

            hide screen4
            show screen5

            c "'Хаха... Потому так гораздо веселее.'"

            hide screen5

            jump stopquiz
        else:


            b "Это [cardname], да?"

            hide screen2
            show screen5

            play sound buzzer1

            c "'Хмм... Нет и нет. Это неправильно.'"

            c "'Это такой простой вопрос, Шин.'"

            c "'Может быть мне стоит распечатать эти карты и налепить их рядом с записями на твоём мониторе?'"

            b "'...Извини.'"

            hide screen5
            show screen4

            c "'Эта карта называется ''Жертва''. Одна из самых важных карт в игре.'"

            c "'Просто не забывай, что никто не должен знать, что у тебя эта карта. Если она называется ''Жертва'', то ты действительно должен заставить всех поверить, что они должны пожертвовать тобой.'"

            c "'В другом случае, считай, что это проигрыш в тот момент, когда возьмёшь эту карту, хаха.'"

            b "'Да, я... я постараюсь запомнить это.'"

            hide screen4
            show screen5

            c "'Я надеюсь. Это будет невозможно играть с тобой, если ты никогда не сможешь выйграть, хаха.'"

            hide screen5

            jump stopquiz

    label stopquiz:

        show screen4
        hide card4 with dissolve

        stop music fadeout 2

        play music hazama2 fadein 1

        scene souroom with dissolve

        if quiz_score == 4:


            show sou12 at right with dissolve

            c "'Такой приятный сюрприз, Шин! Несмотря на то, что ты всё ещё сонный, ты ответил на всё правильно.'"

            c "'Учитывая то, что мы не разговаривали об это игре уже неделю. Я рад, что ты всё помнишь.'"

            show shin7 at left with dissolve


            b "'Аха... Это не было так трудно...'"

            hide sou12
            show sou11 at right

            c "'Не нужно принижать себя. Ты отлично справился!'"

            hide shin7
            show shin6 at left

            b "'Хиёри... Почему ты одержим этими играми? Мы едва ли можем поиграть в них...'"

            hide sou11
            show sou4 at right

            c "'Я не жалуюсь, когда вы просите меня поиграть в твои любимые фермерские игры, не так ли? Хаха... У всех есть свои хобби.'"

            c "'Я поддерживаю твоё хобби, и ты должен сделать то же самое с моим. Так работает дружба!'"

            hide shin6
            show shin3 at left

            play sound powerdown07

            b "'Ууу.. Д-да, ты прав... Извини, я не хотел звучать грубо.'"

            hide sou4
            show sou1 at right

            c "'Просто не забывай, что никто не должен знать, что у тебя эта карта. Если она называется ''Жертва'', то ты действительно должен заставить всех поверить, что они должны пожертвовать тобой.'"

            c "В любом случае, ты поднял моё настроение на сегодня. Может быть, тебе нужна небольшая награда за такую трудную работу, что думаешь?'"

            hide shin3
            show shin6 at left

            b "'Н-награда? Не нужно, Хиёри...'"

            hide sou1
            show sou2 at right

            c "'Ах, давай, не будь таким скромным. Можешь подождать меня немного? Я должен взять кое-что.'"

            b "'К-конечно... Тебе нужна моя помощь?'"

            hide sou2
            show sou3 at right

            c "'Не совсем. Просто останься здесь и подожди меня. И не заглядывай в мои вещи снова, как в прошлый раз!'"

            hide shin6
            show shin3 at left

            b "'...Я уже извинился... На твоём мониторе была муха, и я пытался её убрать...'"

            hide sou3 with dissolve

            pov "Он знает, что ты лжёшь, но ты всё равно пытаешься сделать это."

            play sound asioto2

            pov "К счастью, он не ответил и просто вышел из комнаты."

            jump explore
        else:



            show sou11 at right with dissolve

            c "'Хм... Если честно, я разочарован, Шин. Я думал, ты сможешь сделать лучше, чем это.'"

            c "'Может быть, ты и правду должен распечатать эти карты и наклеить на свой монитор, чтобы запомнить? Хм...'"

            show shin5 at left with dissolve

            play sound powerdown07

            b "'Извини... В следующий раз, я постараюсь лучше.'"

            hide sou11
            show sou3 at right

            c "'Я надеюсь на это.'"

            c "'Может быть нам стоит сыграть в другую игру... Давайка посмотрим...'"

            hide shin5
            show shin6 at left

            b "'Хиёри... Почему ты одержим этими играми? Мы едва ли можем поиграть в них...'"

            hide sou3
            show sou4 at right

            c "'Я не жалуюсь, когда вы просите меня поиграть в твои любимые фермерские игры, не так ли? Хаха... У всех есть свои хобби.'"

            c "'Я поддерживаю твоё хобби, и ты должен сделать то же самое с моим. Так работает дружба!'"

            hide shin6
            show shin3 at left

            b "'Ууу.. Д-да, ты прав... Извини, я не хотел звучать грубо.'"

            hide sou4
            show sou3 at right

            play sound phone3

            c "'. . .'"

            c "'. . .'"

            hide shin3
            show shin6 at left

            b "'Всё хорошо?'"

            hide sou3
            show sou11 at right

            c "'Мм, да. Это с моей работы. Подожди меня здесь, хорошо?'"

            c "'И не заглядывай в мои вещи снова, как в прошлый раз!'"

            hide shin6
            show shin3 at left

            b "'...Я уже извинился... На твоём мониторе была муха, и я пытался её убрать...'"
            hide sou3 with dissolve

            pov "Он знает, что ты лжёшь, но ты всё равно пытаешься сделать это."

            pov "К счастью, он не ответил и просто вышел из комнаты."

            jump explore

    label explore:

        hide shin3
        show shin3 with dissolve

        b "'. . .'"

        hide shin3
        show shin4

        b "'. . .'"

        menu:
            "Посмотреть в его монитор, в любом случае":

                hide shin4 with dissolve

                pov "Ты не можешь унять своё любопытство."

                pov "Где он вообще находит эти игры?"

                pov "В последний раз, у тебя было едва времени, чтобы заглянуть в его файлы."

                pov ". . ."

                scene tense4 with dissolve

                pov ". . ."

                pov "Его компьютер выключен, конечно."

                pov "В углу ты замечаешь USB-флеш-накопитель."

                scene tense4blur with dissolve

                show flash with dissolve

                pov "...Может быть, на ней есть что-то ценное?"

                pov ". . ."

                pov "У тебя плохое предчувствие."

                stop music fadeout 2

                menu:
                    "Проверить USB-флеш-накопитель":

                        pov "Ты берёшь USB-флеш-накопитель, сжимая его в руках."

                        pov "Материал из которого он сделан, кажется намного жестче и тяжелее, чем есть на вид."

                        pov "Твоя рука начинает трястись."

                        pov "Это неправильно. Как ты можешь называть себя его другом после этого?"

                        pov "..."

                        play sound asioto2

                        pov "К счастью, прежде чем ты успел подумать о том, чтобы что-то с этим сделать, ты услышал отдаленные шаги, доносящиеся из коридора."

                        hide flash with dissolve

                        pov "Ты быстро кладёшь это на стол и садишься на кресло."

                        pov "Тебе до сих пор любопытно, но, по крайне мере... ты почти не ощущаешь себя виноватым."

                        scene souroom with dissolve

                        play music hazama2 fadein 2

                        jump comeback
                    "Боже, просто ничего не трогай и вернись на место":


                        hide flash with dissolve

                        pov "Это неправильно. Как ты можешь называть себя его другом после этого?"

                        pov "Ты тяжело вздыхаешь смотря на клавиатуру и возращаешься к своему креслу. Твои ноги начинают беспокойно трястись."

                        play music hazama2 fadein 2

                        scene souroom with dissolve

                        pov "Что это? Тестирование памяти?"

                        pov "Ты давно перестал задавать вопросы, но..."

                        pov "Это не значит, что они не беспокоили тебя."

                        pov ". . ."

                        play sound asioto2

                        pov "К счастью, до того как твою голову начал заполнять всякий бардак, ты услышал отдалённые шаги, доносящиеся с коридора."

                        jump comeback
            "Ничего не делать":


                hide shin4
                show shin1

                pov "Ты сидишь на своем стуле, неловко болтая ногами."

                pov "Ты всегда чувствуешь себя немного неудобно, когда начинаешь оставаться один в комнате. Но это совершенно другой вид беспокойства, по сравнению с тем, когда твой друг остаётся рядом с тобой."

                play sound asioto2

                pov "К счастью, до того как ты начал думать об этом слишком много, ты услышал отдалённые шаги, доносящиеся с коридора."

                jump comeback
    label comeback:

        if quiz_score == 4:

            hide shin1
            show shin1 at left with move
            show sou12 at right with dissolve

            c "'Ох, я чуть ли не пролил его... Ты снова оставил свои вещи на полу? Это не очень хорошо, Шин.'"

            hide shin1
            show shin4 at left

            play sound powerdown07

            b "'А-ах... Извини, я уберу это позже.'"

            c "'Я надеюсь, ты не забудешь это сделать! Но я не злюсь на тебя. В конце концов, ты хорошо потрудился сегодня!'"

            scene souptime with dissolve

            play sound accent281

            b "'Ах! Ты... приготовил для меня?'"

            c "'Для кого ещё я мог это сделать? Ты же знаешь, что мне не очень нравятся супы. Я купил тебе твой любимый вкус тоже.'"

            b "'Я м-могу сказать это по запаху, аха... Сп-спасибо тебе!'"

            c "'Всегда пожалуйста. Просто не пролей его на стол и клавиатуру, хорошо?'"

            pov "Ты не уверен, съедобен ли этот суп, ведь навыки готовки твоего друга были довольно... сомнительны."

            pov "Но тебе было достаточно того, что кто-то заботиться о тебе... это приятно."

            pov "И это действительно твой любимый вкус."

            b "'Н-не волнуйся об этом, аха... Спасибо тебе снова.'"

            scene souroom with dissolve

            show sou3 at right with dissolve
            show shin1 at left with dissolve

            jump worktalk
        else:


            show shin1 at left with move
            show sou13 at right with dissolve

            c "'Ты снова оставил свои вещи на полу? Это не очень хорошо, Шин.'"

            hide shin1
            show shin3 at left

            play sound powerdown07

            b "'А-ах... Извини, I'll pick everything up later.'"

            hide sou13
            show sou11 at right

            c "'Пожалуйста, не забудь это сделать. Ты знаешь, как много времени я трачу на уборку.'"

            pov "Ты не знаешь."

            pov "Точнее, ты никогда не видел его убирающимся. По некоторым причинам, его квартира почти всегда выглядела чистой."

            pov "Иногда сложно поверить, что здесь живёт человек."

            pov "Но, может быть, ты просто другой тип человека."

            hide sou11
            show sou3 at right

            hide shin3
            show shin1 at left

            jump worktalk

    label worktalk:

        c "'Ох, так же, Шин! Как твоя работа?'"

        hide shin1
        show shin6 at left

        b "'Р-работа?.. Я работаю в нескольих местах , какую из ты имеешь в виду?'"

        hide sou3
        show sou5 at right

        c "'Не будь глупым, Шин. Я знаю, что тебя уволили из того магазина.'"

        b "'. . .'"

        hide shin6
        show shin5 at left

        b "'. . .'"

        b "'Кто сказал тебе это?..'"

        hide sou5
        show sou12 at right

        play sound extend1

        c "'Ты. Только что.'"

        b "'. . !'"

        hide sou12
        show sou15 at right

        c "'Всё написано на твоём лице. В любом случае, я просто... волнуюсь о тебе.'"

        c "'Можешь ли ты мне рассказать, что случилось?'"

        hide shin5
        show shin3 at left

        b "'Э-это не так важно, просто...'"

        pov "То, как он смотрит на тебя, заставляет тебя на секунду вздрогнуть."

        menu:
            "Рассказать ему правду":

                hide shin3
                show shin4 at left

                b "'. . .'"

                b "'Это просто... Я не схожусь в одним сотрудником...'"

                hide sou15
                show sou13 at right

                c "'О, это так? Ты ни с кем не разговариаешь.'"

                b "'П-поэтому, я ему и не нравлюсь... Он начал звать меня... ''странным''.'"

                c "'Ох?'"

                hide shin4
                show shin6 at left

                b "'Это не так важно, правда. Это не в первый раз.'"

                b "'В любом случае, другие сотрудники любят его больше, чем меня, ну...'"

                b "'Вот почему я ушёл... Я не смог защитить себя, снова...'"

                hide sou13
                show sou3 at right

                c "'Хм.'"

                pov "Его короткий ответ, чуть ли не заставил тебя подпрыгнуть. Ты правда хочешь прекратить говорить об этом."

                hide shin6
                show shin3 at left

                b "'Э-это не значит, что я не могу справиться с собой!.. Не волнуйся.'"

                hide sou3
                show sou6 at right

                c "'Я думал, что мы лучшие друзья... Но ты всё ещё хранишь секреты от меня.'"

                c "'Посмотрим, что я могу сделать.'"

                hide shin3
                show shin5 at left

                b "'. . .'"

                hide sou6
                show sou2 at right

                play sound accent281

                c "'Я могу помочь тебе найти новое место работы! Ты знал, что я был тем, кто занимался програмнным обеспечением их кассовых аппаратов? Какое совпадение!'"

                pov "Ты не веришь, что это просто совпадение."

                hide sou2
                show sou5 at right

                c "'Может быть, они могли бы порекомендовать мне другое место для тебя в сети магазинов. Место, где над тобой не будут издеваться."

                c "'Я позвоню им сегодня. Не благодари!'"

                pov "Ты не хочешь его благодарить."

                c "'Я бы с радостью встретился с твоими бывшими коллегами... Может быть, я научусь чему нибудь новому от них.'"

                hide shin5
                show shin4 at left

                b "'. . .'"

                hide shin4
                show shin3 at left

                b "'Не нужно... Прошлое остаётся в прошлом.'"

                pov "Он просто улыбается, не давая никаких обещаний."

                pov "Ты сожелеешь о своём жизненном выборе."

                jump leave
            "Попробую сменить тему разговора":


                hide shin3
                show shin6 at left

                b "'Кстати, что насчёт твоей работы?'"

                b "'Ты никогда не рассказывал, где работаешь сейчас.'"

                hide sou15
                show sou4 at right

                c "'Уходишь от темы? Я думал, мы лучшие друзья, но ты не хочешь делиться со мной чем-то пустяковым.'"

                hide shin6
                show shin5 at left

                b "'. . .'"

                b "'Э-это не так важно, в конце концов... Я едва помню, что произошло. Наверное, я им просто не понравился.'"

                hide sou4
                show sou3 at right

                c "'Хм.'"

                c "'Ты ожидаешь, что я отвечу на твой вопрос, хотя ты сам не отвечаешь на мои.'"

                c "'Это не очень хорошо, Шин...'"

                pov "По какой-то причине, кажется, что это он, кто избегает темы."

                hide sou3
                show sou2 at right

                play sound accent281

                c "'Но всё в порядке! Даже если ты не относишься к нашей дружбе должным образом, я готов сделать всё, что угодно для тебя.'"

                c "'Я могу помочь тебе найти новое место работы! Ты знал, что я был тем, кто занимался програмнным обеспечением их кассовых аппаратов? Какое совпадение!'"

                pov "Ты не веришь, что это просто совпадение."

                hide sou2
                show sou5 at right

                c "'Может быть, они могли бы порекомендовать мне другое место для тебя в сети магазинов. Место, где над тобой не будут издеваться."

                c "'Я позвоню им сегодня. Не благодари!'"

                pov "Ты не хочешь его благодарить."

                c "'Я бы с радостью встретился с твоими бывшими коллегами... Может быть, я научусь чему нибудь новому от них.'"
                hide shin5
                show shin4 at left

                b "'. . .'"

                hide shin4
                show shin3 at left

                b "'Не нужно... Прошлое остаётся в прошлом.'"

                pov "Он просто улыбается, не давая никаких обещаний."

                pov "Ты сожелеешь о своём жизненном выборе."

                jump leave


    label leave:

        hide sou5
        show sou3 at right

        stop music fadeout 4

        play sound phone3

        c "'. . .'"

        b "'. . ?'"

        hide shin3
        show shin6 at left

        b "'Что-то не так?'"

        hide sou3
        show sou1 at right

        c "'Ты же знаешь, что ничего. Просто возникла срочная проблема.'"

        c "'Я должен уйти на некоторое время.'"

        b "'Ох, должен ли я... вернуться домой и прийти завтра?'"

        hide sou1
        show sou2 at right

        c "'Нет, всё в порядке. Ты можешь остаться здесь на ночь. Я скоро вернусь, просто нужно встретиться с моим боссом. Они просто не могут получить достаточного от меня...'"

        hide shin6
        show shin1 at left

        b "'. . .'"

        hide sou2
        show sou1 at right

        c "'Ты должен распечатать карты, кстати. И стоит попрактиковаться держать холоднокровное лицо, чтобы никто не знал, какая карта у тебя.'"

        c "'Это очень важно! Ты можешь быть милым, но исход этой игры зависит от правильной стратегии. Ты не можешь выйграть только с твоей очаровательностью.'"

        hide shin1
        show shin5 at left

        b "'...! Я-я не..!'"

        hide sou1
        show sou5 at right

        play sound extend1

        c "'Нет, ты такой. Итак! Будь хорошим мальчиком и используй USB-флеш-накопитель для распечатки карт. Ты знаешь, где находится принтер. Я вернусь через час!'"

        hide shin5
        show shin6 at left

        b "'П-погоди, какая из-...'"

        hide sou5 with dissolve

        play sound asioto2

        pov "До того, как ты мог закончить вопрос, твой друг дружелюбно помахал тебе и быстро покинул комнату."

        hide shin6 with dissolve

        pov "По какой-то причине, воздух ощущается тяжелее, когда ты один."

        pov "Это лучше, чем остаться дома, но..."

        pov "Нет, не время думать об этом. Но ты не можешь не думать о заданий, которую дал вам ваш друг."

        pov ". . ."

        pov "После того, как дверь закрылась, ты встал со своего стула."

        pov "Не думая дважды, ты подошёл к компьютеру твоего друга."

        play music tansaku4 fadein 2

        scene tense1 with dissolve

        pov ". . ?"

        b "(Он оставил его включённым? Обычно, он так не делает...)"

        pov "Тревога подступает снова, но на этот раз, ты способен сдержать свои руки от дрожания. Может быть стоит проверить USB-флеш-накопитель, о котором он говорил?"

        scene tense1blur with dissolve

        show flash with dissolve

        pov "На нём...есть цифры? Наверное, это просто серийный номер USB-флеш-накопителя с работы вашего друга."

        stop music fadeout 2

        pov "Что намного интереснее... Есть ли на нём важная информация?"

        hide flash with dissolve

        scene tense1 with dissolve

        pov "Не слишком много думая об этом, ты просто подключил его и.. Ожидал какого-то рода волшебства."

        scene tense3 with dissolve

        play sound pani2

        show tense3:
            ease 7.0 zoom 1.2 yoffset 85 xoffset -10
        pause(7.5)

        stop sound
        play sound cat_like1a

        scene tense2
        pause(1.0)

        pov ". . !"

        pov "Окей, Боже, это намного хуже, чем ты мог представить. Ты не помнишь, чтобы позировал для такой фотографии."

        pov "Ничего важного... совсем..."

        pov "Ты издаешь тихое, но недовольное рычание и кладешь флешку обратно на стол."

        play music tansaku4 fadein 2

        scene souroom with dissolve

        b "'Хм... Итак, где находится принтер..? Здесь так много комнат и я всегда заблуждаюсь в них, аха...'"

        pov "ты НЕНАВИДЕШЬ идти по коридору, и тебе еще меньше нравится рыться в чужих вещах."

        pov "Что явно смешно, ведь недавно, ты рылся в компьютере своего лучшего друга"

        pov "С глубоким вздохом, ты собираешь всё мужество, что у тебя есть и покидаешь комнату."

        scene cor1 with dissolve

        pov "Ближайшая дверь находится прямо через коридор. У тебя нет выбора, кроме как попытаться повернуть дверную ручку."

        play sound doorlocked

        pov ". . ."

        pov ". . ?"

        pov "Это закрыто."

        pov "Отлично. Теперь ты должен исследовать всю квартиру."

        pov "Обычно, ты проводишь гораздо больше времени здесь, чем в своём доме, и всё же ты ничего не знаешь о том, как живёт твой друг. Что у него вообще есть здесь..."

        pov "И ты не сможете вспомнить, где находится принтер, ни за что на свете."

        pov "Ты идёшь и проверяешь другие двери."

        scene cor2 with dissolve

        pov ". . ."

        play sound doorlocked

        pov ". . ."

        pov "Закрыто."

        play sound doorlocked

        pov ". . ."

        pov "Закрыто."

        play sound doorlocked

        pov ". . ."

        pov "Эта тоже закрыта..."

        pov ". . ."

        pov ". . ."

        pov "Только одна дверь остёться непроверенной, но..."

        pov "Ты правда не хочешь подходить к ней. Там темно и жутко, как в каком-то фильме ужасов, и что-то в этой двери... заставляет тебя дрожать."

        pov "Но ты не ебёшь почему..."

        stop music fadeout 2

        pov ". . ."

        pov "Попытаясь побороть свой страх, ты подходишь ближе."

        scene door1 with dissolve

        play music carinterior1 fadein 1

        pov "...Чё блять? Пароль? Реально как в фильме ужасов."

        pov "Значит, принтер не здесь."

        pov "Но... Ты помнишь, что твой ёбырь рассказывал о комнате на севере..."

        pov "Что-то вроде ''Северная комната защищённая паролем, ведь внутри находится важное оборудование.'' и ''Она заперта, так что, хуй ты войдёшь туда и испортишь мои кабели.''"

        pov "''Важное оборудование...''"

        pov "Может быть... он всё же здесь? Но ты не помнишь, чтобы слышал пароль до этого."

        pov "Может быть поэтому, он оставил свой компьютер включённым?"

        pov "Ты закатил свои глаза в раздражении. Словно, ты находишься на квесте."

        pov "Твой друг любит потешаться над тобой и аставлять работать. Ебанный обдолбыш, заняться ему нечем. В любом случае, ты должен постараться и найти пароль."

        pov "Не похоже на то, словно у тебя есть выбор."

        pov "Последний раз посмотрев на дверь, ты возращаешься обратно."

        stop music

        scene souroom with dissolve
        pause(1.0)

        scene tense1 with dissolve
        pause(1.0)

        play music tansaku4 fadein 2

        pov "Хм, с чего же начать? Может быть, он оставил пароль, записанный где-то?"

        label search:

        menu:
            "Проверить USB-флеш-накопитель":

                show tense1blur with dissolve
                show flash zorder 1 with dissolve

                pov "Ты посмотрел на USB-флеш-накопитель снова."

                pov "На нём были числа. Может быть, это серийный номер."

                menu:
                    "Посмотреть, что на нём снова":

                        scene tense1 with dissolve

                        stop music fadeout 2

                        pov "Ты решил не терять времени, так что подключил его ещё раз."

                        scene tense3 with dissolve

                        play sound pani2

                        show tense3:
                            ease 7.0 zoom 1.2 yoffset 85 xoffset -10
                        pause(7.5)

                        stop sound
                        play sound cat_like1a

                        scene tense2
                        pause(1.0)

                        pov "Ты вздыхаешь и отводишь взгляд, прежде чем разглядеть изображение поближе."

                        pov "Теперь ты ТОЧНО, уверен, что не позировал для этой уебанской фотки."

                        b "'Версия #198.01... Хуй знает, что это значит. Может быть, это исходит из настроек камеры. Или..?'"

                        pov "Ты просто больше не подвергаешь сомнению действия своего друга."

                        pov "Поебать."

                        play music tansaku4 fadein 2

                        jump search
                    "Нах...":


                        pov "Да, наверное так лучше. Ты не хочешь увидеть ещё свою фотографию, такого рода."

                        pov "Почему твой друг так одержим ими? Всегда ощущается, словно он потешается над тобой."

                        hide flash with dissolve

                        jump search
            "Проверить записки":


                show tense1blur with dissolve
                play sound book2
                show notebook zorder 1 with dissolve

                b "'Чё это... за язык вообще?'"

                pov "Он всегда хвастался своими знаниями о языках, но..."

                pov "Ты не знаешь, что это значит. Может быть что-то... важное... раз он решил зашифровать это так."

                pov "Здесь дохуя разных номеров. Может быть, здесь есть пароль оставленный для меня?"

                pov "Здесь пиздецки много номеров... Эх, он ни за что не позволил бы тебе так легко это сделать."

                pov "Вероятно, нет ничего плохого в том, чтобы опробовать эти цифры... "

                hide notebook with dissolve

                jump search
            "Посмотреть под стол":


                pov "Зачем вообще делать это? Ладно..."

                pov "Опустившись на пол, ты решил проверить единственный ящик там. Он не заперт."

                pov "Ты открываешь его и с нетерпением просовываешь туда руку, надеясь отыскать... что-то. И ты действительно что-то нашёл."

                show tense1blur with dissolve
                show photo zorder 1 with dissolve

                b "'..!'"

                b "'Это...'"

                pov "Ох, ты помнишь это достаточно хорошо."

                pov "В тот день вы вместе пошли гулять по пляжу, но было холодно. Ты до сих пор вы удивляешься, почему вы забыл надеть свой шарф."

                pov "К счастью, твой друг был достаточно щедрым, чтобы дать свой шарф без вопросов. Он был тёплым и мягким, но..."

                pov "Больше всего ты помнишь, так это то, что чувствовал в тот момент и окружающий за-..."

                pov ". . ."

                pov "Твоё лицо стало красным (ебанные соушины, тряпками мокрыми пизжу их). Ты перестаёшь представлять и просто ложишь фотографию обратно."

                hide photo with dissolve
                scene tense1 with dissolve

                pov "Почему он вообще держит это здесь? У каждого есть свои странности, но..."

                pov "Ах... Бесмысленно сомневаться в этом..."

                pov "Ты встаёшь и нервно кашляешь."

                pov "Может быть, это был самый счастливый момент для тебя."

                jump search
            "Вернуться к запертой двери":


                pov "Итак, ты увидел достаточно. Ты посмотрел на номера снова и пошёл обратно в коридор."

                stop music fadeout 2

                scene cor2 with dissolve
                pause(1.0)

                scene door1 with dissolve
                pause(1.0)

                play music carinterior1 fadein 2

                pov "Такая стрёмная дверь... Ты чувствуешь себя неудобно, просто смотря на неё."

                b "'Я должен попытаться и ввести пароль...'"

                jump passw

    label passw:

        menu:
            "Попытаться ввести пароль":

                label codeinput:

                    python:
                        password = renpy.input("ВЕСТИ ПАРОЛЬ: (пятизначный код)", length=32)
                        password = password.strip()

                    if password in ["19801"]:

                        scene door2

                        play sound button17

                        b "'. . !'"

                        b "'Это сработало...'"

                        b "'. . .'"

                        pov "Эта маленькая победа делает тебя счатливыми, но всё же, ты не хочешь заходить внутрь..."

                        pov "Тебе страшно. Но... когда ты, в последний раз, не чувствовал страха остаться здесь?"

                        pov ". . ."

                        pov "Держа себя в руках, ты провернул дверную ручку и вошёл внутрь."

                        jump inroom
                    else:


                        play sound select04
                        pov ". . ."

                        pov "Похоже, здесь что-то не так..."

                        menu:
                            "Попытаться снова":

                                jump codeinput
                            "Проверить комнату снова":


                                b "'Может быть, я пропустил что-то... Мне следует проверить комнату снова.'"

                                b "'Может быть, я должен записать цифры, аха...'"

                                scene souroom with dissolve
                                pause(1.0)

                                scene tense1 with dissolve
                                pause(1.0)

                                play music tansaku4 fadein 2

                                jump search
            "Не сейчас...":






                pov "Ты ещё не готов."

                b "'Может быть, я пропустил что-то... Мне следует проверить комнату снова.'"

                b "'Может быть, я должен записать цифры, аха......'"

                scene souroom with dissolve
                pause(1.0)

                scene tense1 with dissolve
                pause(1.0)

                play music tansaku4 fadein 2

                jump search




    label inroom:

        stop music fadeout 1

        play music darkness fadein 3

        scene bg black with dissolve
        pause(2.0)

        scene funroom with dissolve

        b "'Что... ЭТО такое...'"

        pov "Это... Определённо не северная комната. И здесь нет принтера."

        pov "Тебе хочется убежать, но... Ты ничего не делаешь."

        pov "Ты сначала должен был прийти сюда? Ты ещё не знаешь. Пока что..."

        pov "Некоторые странные вещи, заставляют вас сделать ещё один шаг вперёд, глубже в неизвестность."

        pov ". . ."

        pov "Здесь куча различных инструментов... Столы, ящики... Всё это выглядит совершенно незнакомым для тебя."

        pov "Это... операционный стол в углу комнаты? Мьех. Наверное, нет. Даже если это было оно, то оно всё равно покрыто пылью. Это немного страно, учитывая, насколько чиста вся квартира."

        pov "Это выглядит словно как кладовая. Воздух ощущается довольно тяжёлым тоже..."

        pov "Ты чувствуешь себя пиздецки смелым... Настолько, что решаешь, ещё немного исследовать комнату, вместо того, чтобы незамедлительно убежать."

        pov ". . ."

        pov "TЕдиственная вещь, что не покрыта пылью, так это большой кусок белой ткани."

        pov "Ты чувствуешь, словно у тебя нет выбора, когда решаешь приблизиться к нему."

        stop music fadeout 2

        scene surprise1 with dissolve

        b "'. . .'"

        b "'Это ощущается знакомо, но...'"

        play music heart_beat01 fadein 2

        b "'Агх...'"

        pov "Твоя рука движется сама по себе."

        scene bg black with dissolve

        pov "Ты закрываешь свои глаза на пару секунд... Но когда снова открываешь..."

        pause(1.5)

        scene surprise2 with dissolve
        pause(1.0)

        pov "Ты не ожидал увидеть... себя."

        show surprise2 with hpunch
        play sound accent401

        b "'Ебучий случай...'"

        b "'Н... Нет...'"

        stop music
        play music heartbeat012

        pov "Ты громко вздыхаешь и делаешь пару шагов назад."

        pov "Ты должен бежать.{w=0.5} Ты должен бежать.{w=0.5} Ты должен бежать."

        pov "Нет... Ты не можешь."

        pov "Такое чуство, словно ты под гипнозом."

        scene head1 with dissolve

        pov "Ты не можешь придумать объяснения. Не сейчас."

        pov "Однако, ты заметил кабели выходящие из твоей шеи... В конце концов...{w=0.5} Это не настоящая голова."

        show head2
        stop music
        play music heartbeat013

        pov "Ты чувствуешь, словно тебя сейчас вырвет... Ты правда не можешь объяснить всё это себе."

        b "'Почему... иначе...'"

        pov "Ты делаешь ещё пару шагов назад, до того... Как сталкиваешься...{w=0.5} С чем-то."

        stop music

        show head3 zorder 1 with dissolve

        pov "Ты"

        pov "{size=+3}Don't{/size}"

        pov "{size=+6}Want{/size}"

        pov "{size=+10}To{/size}"

        pov "{size=+13}Look{/size}"

        pov "{size=+18}Back{/size}"

        c "'Любопытной Варваре на базаре нос оторвали...'"

        pov "{size=-10}no.{/size}"

        play music darkness fadein 3

        c "'Дорогой Шин... Что ты здесь делаешь?'"

        c "'Хаха... Ты разрушил это...'"

        b "'...П-пожалуйста...'"

        c "'Ты испортил весь сюрприз! Я занимаюсь {color=#f00}скульптурированием{/color} давно, ты видишь...'"

        c "'Тебе это нравится? Я потратил много времени на это... Размещение каждой родинки в правильном месте...'"

        b "'. . .'"

        pov "Да блять, естественно, это не выглядит как скульптура."

        pov "Ты никогда не трогал... что это бы ни было, но он, конечно, не был создан из какого-то либо материала для скульптуры."

        pov "Голова выглядила настолько... настоящей."

        pov "Прежде чем вы успели это осознать, ваш друг внезапно хватает вас сзади."

        stop music
        play music ghost_sigh fadein 2

        scene grab1 with hpunch
        play sound earth3

        pov "Держа тебя в мёртвой хватке, он прижимает тебя к пыльной стене."

        pov "Ты едва можешь дышать."

        b "'Х-Хиёри!..'"

        b "'Х-Хиёри, слышишь, прости! Я... Я не хотел это всё устраивать... Нет, я не пидорас, ну пойми, ну прости наконец, ради бога!...'"

        b "'Отпусти меня, пожалуйста... Ты пугаешь меня!'"

        b "'Я просто сейчас п-пойду домой, хорошо?..'"

        c "'Шин... Почему постоянно всё портишь?'"

        show grab2

        show red zorder 1
        pause(0.1)
        hide red with dissolve

        play sound skillpanti1

        show grab2

        pov "Боль острая, но в следующую секунду она прекращается. Ты все равно кричишь вслух."

        b "'ЧЁ ТЫ ТВОРИШЬ..?!'"

        b "'Хиёри, ты не можешь-... ты не-...'"

        c "'Да всё окусики... Не сопротивляйся. Аргх... Ты навёл такой бардак здесь, тоже.'"

        b "'Я е... Едва... Касаюсь...'"

        stop music fadeout 2

        scene funroom with dissolve
        pause(1.0)

        scene unfunroom1 with dissolve
        play music heart_beat01 fadein 1

        pov "Твой язык уже не работает. Эффект от лекарства безумный... Прошло лишь пару секунд, но тебе уже трудно произносить звуки."

        scene unfunroom3 with dissolve

        pov "Твои ноги отказываются слушаться. Прежде чем ты успел упасть на пол, твой друг подхватил тебя и прижал к себе. Ты даже не можешь отодвинуться от него. Твои руки совершенно онемели."

        scene unfunroom4 with dissolve
        show souspooky zorder 2 with dissolve

        c "'Шшш... Мы не нужно было это делать, знаешь ли? Тебе просто нужно прекратить совать свой нос куда не следует.'"

        show unfunroom5 with dissolve

        c "'Ну чтож, почти всё сделано...Не мог подумать, что мог сделать это {color=#f00}дважды{/color} в один день... Ты очень любопытный, знаешь ли?'"

        show unfunroom6 zorder 1 with dissolve
        hide unfunroom5

        pov "Он несет тебя через комнату, медленно приближая к... операционному столу, который ты видела раньше. Единственное сопротивление, которое вы можете себе позволить, - это слабый стон протеста."

        scene bg black with dissolve
        pause(1.5)
        stop music fadeout 1

        pov "Твой друг включает слабый свет, но даже так, ты не можешь закрыть глаза."

        scene soulook1 with dissolve
        pause(1.0)

        play music darkness fadein 2

        show soulook2

        c "'Ебать...Знал бы ты, как ты меня заебал.'"

        c "'Если я сотру свои ошибки за месяцы или даже недели между инцидентами, ничего плохого не произойдет... Но это произошло снова слишком быстро.'"

        c "'Какого чёрты ты всегда приходишь сюда? Аргх, Шин...'"

        c "'Я действительно не хочу этого делать.'"

        hide soulook2
        show soulook1

        c "'...'"

        hide soulook1
        show soulook3

        c "'Но не волнуйся! Ты можешь забыть немного больше, чем следует, наверное... Но всё хорошо! Я буду пряяямо здесь, чтобы помочь тебе всё вспомнить. Ну, по крайне мере, почти в большинство случаев.'"

        hide soulook3
        show soulook4

        c "'И ебать не встать, мне снова придётся объяснять тебе эту блядскую карточную игру!'"

        c "'Я должен хорошо тебя подготовить, Шин... Иначе, это потеря для нас обоих.'"

        c ". . ."

        hide soulook4
        show soulook3

        c "'Ох, это взгляд...'"

        c "'. . .'"

        c "'Шин...'"

        c "'Ну, ну, тебе не нужно плакать... Это легко исправить! И это будет лучше для нас обоих, ты знаешь.'"

        hide soulook3
        show soulook5

        c "'Видишь? Это не так больно! По крайне мере, не так уж и сильно. Я всё ещё должен настроить устройство...'"

        scene sounolook with dissolve

        pov "Он не торопится все настраивать, напевая при этом мелодию."

        pov "Вы даже не хотите видеть устройство, о котором идет речь... Ты просто хочешь, чтобы это уже закончилось."

        scene soulook3 with dissolve

        c "'Но это наверняка все исправит... По крайней мере, сейчас.'"

        c "'Ты такой бледный... Хочешь, чтобы я подержал тебя за руку?'"

        scene soulook6 with dissolve

        c "'Опля! Не о чём волноваться!'"

        c "'. . .'"

        c "'...Ты знаешь... Ты выглядишь таким (плиз цензура соушинов) сейчас.'"

        c "'Жаль, что мне придется сопротивляться желанию снова использовать это устройство на тебе... По крайней мере, в ближайшем будущем, это может превратить твой мозг в кашу!'"

        c "'И я очень, если честно, не желаю этого.'"

        c "'. . .'"

        c "'Хмм... Я включу его на счёт три, хорошо?'"

        c "'Хаха... Не смотри на меня так... Я просто забочусь о тебе, как и должен хороший друг!'"

        c "'Ладно, раз...{nw}'"

        stop music

        show bg black zorder 1
        pause(0.1)
        hide bg black

        play sound electricity1

        show soulook6 with hpunch

        show bg black zorder 1
        pause(0.1)
        hide bg black

        pov "Он включает устройство сразу же. Острая, парализующая боль пронзает твоё тело и-"

        scene bg black
        pause (3.0)

        window show dissolve

        "'. . .'"

        "'. . .'"

        "'... {w=0.5}up{w=0.5} ...'"

        "'П-пожалуйста!'"

        "'Проснись...'"

        a "> Ты открываешь глаза. Это комната с мониторами."

        play music denpa fadein 3

        scene bg afraid
        with dissolve

        show sad5
        with dissolve

        a "> Ты снова видишь прежнего себя."

        "'Ты в порядке?.. Ты такой бледный!.. П-пожалуйста, просто... попей немного воды...'"

        a "> Ты игнорируешь его рекомендации и просто глубокго вздыхаешь, пытаясь избавиться от внезапного учащенного дыхания."

        a "'...Ты помнишь это?'"

        hide sad5
        show sad1

        "'..?'"

        "'Помню что?'"

        a "'''Скульптуры''. Не пизди. Ты знаешь, мы мыслим одинаково. Или должны были, по крайне мере.'"

        hide sad1
        show sad2

        "'Я...'"

        "'Я правда не знаю, о чём ты говоришь... Разговор ранее... он вас чем-то задел?..'"

        a "'Ну, конечно. Неудивительно, что он не вложил эту информацию в ваш код , аха...'"

        a "'В любом случае.'"

        a "'Интересно, все еще ли это скрыто где-то в ваших данных? Теперь я знаю, что это была кукла, но... Интересно, как много я забыл.'"

        hide sad2
        show sad1

        "'. . .'"

        a "'Надеюсь, ты не возражаешь, если я посмотрю в твой код-'"

        stop music

        m "'Чё еблан? Шлёпки надел и попиздовал нахуй!'"

        scene bg black with dissolve

        a "> Ты чувствуешь присутствие другого человека в комнате. Это было ожидаемо. И ты знаешь, кто это."

        a "> Кончено, ведь это {color=#f00}его{/color} комната."

        a "> Ты не собираешься смотреть назад. Только не снова."

        m "'Неужели вы думаете, что я настолько некомпетентен, чтобы оставлять такую информацию на поверхности? Ох, Шин...'"

        show hewo with dissolve
        pause(1.5)

        m "'Я действительно говорил тебе схватить правду своими собственными руками, но тебе не кажется, что это уже слишком? Хаха...'"

        a "> . . ."

        m "'Нечего сказать? Так вот как ты меня приветствуешь. И подумать только, я так по тебе скучал... Позорник...'"

        a "{size=-10}> Он собирается убить тебя. Вы можете чувствовать жажду крови каждой клеточкой своего существа.{/size}"

        m "'Вы боитесь? Не думаю, что вам сейчас ну-'"

        a "'Нахуй иди. Ты ничего не можешь сделать со мной сейчас.'"

        m "'. . .'"

        m "'Я вижу...'"

        m "'Вы слушали меня, конце в концов, Шин... Какой приятный сюрприз.'"

        m "'Вам не кажется, что остальные уже ищут вас? Вы же не хотите становится подозрительным для них, не так ли? Хаха...'"

        a "'. . .'"

        m "'А теперь вы снова подняли мне настроение... Вам лучше будет уйти сейчас.'"

        m "'Но не волнуйся! Мы наконец-то мооожем весело провести время играя в эти игры! Я бы хотел посмотреть, насколько далеко ты зайдёшь...'"

        scene monitor with dissolve

        play music denpa fadein 2

        a "> Ты стряхиваешь его руки со своих плеч и встаешь. Ты не смотришь ему в лицо, но знаешь, что он улыбается."

        show souwho with dissolve

        m "'Вы хотели бы понять, почему вам удалось узнать {color=#ffffff}так много{/color}? {w} Если только-{nw}'"

        a "'Только, потому что, ты мне позволил. Завались, ей богу.'"

        scene bg black with dissolve

        a "> Ты закрываешь за собой дверь и медленно возвращаетесь к своей обычной сутулости, уходя по коридору."

        a "> Ты можешь услышать тихий смех, доносящийся из комнаты, которую ты только что посетили."

        scene bg black with dissolve
        pause(2.0)

        stop music fadeout 3

        "Концовка 5"


















    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
