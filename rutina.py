#Se simplifica el llamado de algunos comandos
armor=armor_ctrl 
media=media_ctrl
led=led_ctrl
define=rm_define
led=led_ctrl
media=media_ctrl
define=rm_define
#Se definen tiempos
second,milli_second=1,.1
l1,l2=0,255 #Se simplifica el realizar combinaciones RGB para colores a futuro
second,delay=1,.1

#Combinaciones utilizadas en la segunda parte
RGB=[
    [],         
    [l2,l1,l1], 
    [l1,l1,l2], 
    [l2,l1,l1], 
    [l1,l1,l2], 
    [l2,l1,l1], 
    [l1,l1,l2], 
    [l2,l1,l1], 
    [l1,l1,l2], 
    ]



def start():
   
    #____________________________Parte 1:_______________________________________________________________
    chassis_ctrl.set_trans_speed(3) #Definir la velocidad a la que se desplazará el chasis
    #Habilitar el chasis
    chassis_ctrl.enable_stick_overlay() 
    #Encender Leds
    led_ctrl.set_top_led(rm_define.armor_top_all, l2,l1,l2, rm_define.effect_marquee)  
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, l2,l1,l2, rm_define.effect_breath)
    #hacer que el chasis se mueva hacia delante un metro
    chassis_ctrl.move_with_distance(0, 1)
    #hacer que el chasis se mueva hacia atras un metro
    chassis_ctrl.move_with_distance(180, 1) 
    media_ctrl.play_sound(rm_define.media_sound_count_down)
    #Cambio de color
    led_ctrl.set_top_led(rm_define.armor_top_all, l1,l2,l2, rm_define.effect_marquee)  # 
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, l1,l2,l2, rm_define.effect_breath)
    #Mover el robot hacia los lados
    chassis_ctrl.move_with_distance(90, 0.8)
    chassis_ctrl.move_with_distance(-90, 0.8)
    #_________________________Parte2____________________________________________
    ciclo = 0 #para poder salir del ciclo
    while ciclo < 12:
        ciclo = ciclo +1
        led_ctrl.gun_led_on()  #Enciende la pistola laser
        #Ciclo que enciende y apaga rápidamente luces azules y rojas simulando una torreta de policia
        for i in range(1,9):
            led.set_top_led(define.armor_top_all,
            RGB[i][0],RGB[i][1],RGB[i][2],define.effect_always_off)
            led.set_single_led(define.armor_top_all,
            [i],define.effect_always_on)

            led.set_bottom_led(define.armor_bottom_all,
            RGB[-i][0],RGB[-i][1],RGB[-i][2],define.effect_always_on)
            led_ctrl.gun_led_off() #Apaga la pistola laser
    #_________________________Parte3____________________________________________
    #Fijar los colores en azul y rojo mientras se desplazará con un efecto de flash
    led_ctrl.set_bottom_led(rm_define.armor_bottom_front, l1,l1,l2, rm_define.effect_flash)  
    led_ctrl.set_bottom_led(rm_define.armor_bottom_back, l1,l1,l2, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_right, l2,l1,l1, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_left, l2,l1,l1, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_left, l2,l1,l1, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_left, l2,l1,l2, rm_define.effect_flash)

    chassis_ctrl.enable_stick_overlay() #Habilitaar chasis
    media_ctrl.play_sound(rm_define.media_sound_scanning) #eimitir sonido
    chassis_ctrl.set_trans_speed(3.5)  # Velocidad alta para el efecto de drifting
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)  # Color rojo durante el drifting

    # Hacer que el robot se mueva hacia adelante
    chassis_ctrl.move_with_distance(0, 2.5)  # Movimiento lineal hacia adelante
    chassis_ctrl.move_with_speed(3, 1, 340) #Drifteo


    time.sleep(0.5) #wait de 0.5 s, el cual es tiempo suficiente para que gire 180 grados
    chassis_ctrl.move_with_speed(0, 0, 0) #Detener chassis para que no se vaya de largo o hacia otro lado
    time.sleep(0.5) #Otro wait para evitar que la inercia interfiera en la siguiente acción
    # Repetir lo anterior para el otro lado
    chassis_ctrl.move_with_distance(0, 2.9)
    chassis_ctrl.move_with_speed(3, 1, 340)
    time.sleep(0.5) #Contemplar cambiar de 0.5 a 1 segundo para que de la vuelta completa
    #Parar rotacion y translación
    chassis_ctrl.move_with_speed(0, 0, 0)
    time.sleep(0.2)
    chassis_ctrl.move_with_distance(0, 0)
    #______________________________________Parte4________________________________________________________________________
    gimbal_ctrl.set_rotate_speed(400) #Definir velocidad de rotación del gimbal
    chassis_ctrl.set_trans_speed(1)  #definir velocidad de rotación del chassis 
    rm_define.robot_mode_free #Definir que el chassis y gimbal se muevan independientemente
    media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate) #sonido que hará cada que gira el gimbal
    #El chassis comienza a describir un cuadrado mientras el gimbal mira siempre hacia afuera del mismo
    gimbal_ctrl.set_follow_chassis_offset(180) 
    chassis_ctrl.move_with_distance(90, 1)
    media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate)
    gimbal_ctrl.set_follow_chassis_offset(80)
    chassis_ctrl.move_with_distance(0, 1)
    media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate)
    gimbal_ctrl.set_follow_chassis_offset(-10)
    chassis_ctrl.move_with_distance(-90, 1)
    media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate)
    gimbal_ctrl.set_follow_chassis_offset(-100)
    chassis_ctrl.move_with_distance(180, 1)
 
#_____________________________Parte5___________________________________________________
    vision_ctrl.enable_detection(rm_define.vision_detection_people) #Activar la detección de personas
    vision_ctrl.set_marker_detection_distance(1) #definir el rango de detección en un metro

    vision_ctrl.cond_wait(rm_define.cond_recognized_people) #Esperar a que reconozca a una persona

    media_ctrl.play_sound(rm_define.media_sound_recognize_success) #emitir sonido
    gimbal_ctrl.set_rotate_speed(400) #definir velocidad de rotacion

    #En esta parte el gimbal gira de lado a lado haciendo una especie de NO con la cabeza
    #Ya que indica que no ataca humanos
    gimbal_ctrl.set_follow_chassis_offset(45)
    gimbal_ctrl.set_follow_chassis_offset(-45)
    gimbal_ctrl.set_follow_chassis_offset(45)
    gimbal_ctrl.set_follow_chassis_offset(-45)
    gimbal_ctrl.set_follow_chassis_offset(45)
    gimbal_ctrl.set_follow_chassis_offset(-45)
    gimbal_ctrl.set_follow_chassis_offset(45)
    gimbal_ctrl.set_follow_chassis_offset(-45)
    gimbal_ctrl.set_follow_chassis_offset(45)
    gimbal_ctrl.set_follow_chassis_offset(-45)

    #____________________________Parte6___________________________________________________________________________
    armor.set_hit_sensitivity(10) #establecer la sensibilidad de golpes
    led.turn_off(define.armor_all) #apagar lasluces de la armadura por un segundo
    time.sleep(second)

    #Este ciclo se ejecutara hasta que reciba un golpe en cualquier parte del chassis
    golpes = 0
    while golpes < 1:
        while True:
            led.set_top_led(define.armor_top_right,l1,l1,l2,define.effect_always_on)
            led.set_top_led(define.armor_top_left,l2,l2,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_front,l1,l2,l2,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_back,l2,l1,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_right,l1,l2,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_left,l2,l1,l2,define.effect_always_on)
            media.play_sound(define.media_sound_recognize_success,wait_for_complete_flag=True)

            led.set_top_led(define.armor_top_right,l2,l2,l1,define.effect_always_on)
            led.set_top_led(define.armor_top_left,l1,l1,l2,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_front,l2,l1,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_back,l1,l2,l2,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_right,l2,l1,l2,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_left,l1,l2,l1,define.effect_always_on)
            media.play_sound(define.media_sound_recognize_success,wait_for_complete_flag=True)

            led.set_bottom_led(define.armor_bottom_front,l1,l2,l2,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_back,l2,l1,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_right,l1,l2,l1,define.effect_always_on)
            led.set_bottom_led(define.armor_bottom_left,l2,l1,l2,define.effect_always_on)



def armor_hit_detection_all(msg):   

    #Activa los colores de torreta de policia
    led_ctrl.set_bottom_led(rm_define.armor_bottom_front, l1,l1,l2, rm_define.effect_flash)  
    led_ctrl.set_bottom_led(rm_define.armor_bottom_back, l1,l1,l2, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_right, l2,l1,l1, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_left, l2,l1,l1, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_left, l2,l1,l1, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_left, l2,l1,l2, rm_define.effect_flash)

    chassis_ctrl.set_trans_speed(3)   #Define la velocidad del chassis
    media.play_sound(define.media_sound_attacked,wait_for_complete_flag=False) #Emite un sonido
    gimbal_ctrl.set_rotate_speed(500) #Define la velociad de rotacion del chassis
    gimbal_ctrl.set_follow_chassis_offset(180) #Indica que gire 180 grados el gimbal
    led_ctrl.gun_led_on()    #Enciende la pistola led
    chassis_ctrl.move_with_distance(-45, 2)  #se mueve en diagonal durante dos metros
    gun_ctrl.set_fire_count(8) #Fijar los disparos en 8 por segundo
    gun_ctrl.fire_continuous() #disparar  
    time.sleep(2)
    golpes = golpes + 1 #Suma para salir del ciclo



