## Train ticket Story 1
* _greet
    - utter_greet
* _tickets_order
    - utter_ticket_sort
* _tickets_order[ticket=火车票]
    - utter_ticket_place
* _tickets_order[place=上海]
    - utter_ticket_number
* _tickets_order[number=2]
    - utter_ticket_affirm
* _goodbye
    - utter_goodbye
    - export
    
## Train ticket Story 2
* _greet
    - utter_greet
* _tickets_order
    - utter_ticket_sort
* _tickets_order[ticket=车票]
    - utter_ticket_place
* _tickets_order[place=北京]
    - utter_ticket_number
* _tickets_order[number=10]
    - utter_ticket_affirm
* _goodbye
    - utter_goodbye
    - export
    
## Train ticket Story 3
* _greet
    - utter_greet
* _tickets_order
    - utter_ticket_sort
* _tickets_order[ticket=火车票]
    - utter_ticket_place
* _tickets_order[place=宁波]
    - utter_ticket_number
* _tickets_order[number=6]
    - utter_ticket_affirm
* _goodbye
    - utter_goodbye
    - export

## Plane ticket Story 1
* _greet
    - utter_greet
* _tickets_order
    - utter_ticket_sort
* _tickets_order[ticket=机票]
    - utter_ticket_place
* _tickets_order[place=北京]
    - utter_ticket_number
* _tickets_order[number=4]
    - utter_ticket_affirm
* _goodbye
    - utter_goodbye
    - export
    
## Plane ticket Story 2
* _greet
    - utter_greet
* _tickets_order
    - utter_ticket_sort
* _tickets_order[ticket=机票]
    - utter_ticket_place
* _tickets_order[place=宁波]
    - utter_ticket_number
* _tickets_order[number=1]
    - utter_ticket_affirm
* _goodbye
    - utter_goodbye
    - export
    
## Plane ticket Story 3
* _greet
    - utter_greet
* _tickets_order
    - utter_ticket_sort
* _tickets_order[ticket=飞机票]
    - utter_ticket_place
* _tickets_order[place=上海]
    - utter_ticket_number
* _tickets_order[number=3]
    - utter_ticket_affirm
* _goodbye
    - utter_goodbye
    - export

## say goodbye
* _goodbye
  - utter_goodbye