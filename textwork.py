from typing import List

bells = {1: "8:00 - 8:40",
         2: "8:50 - 9:30",
         3: "9:45 - 10:25",
         4: "10:40 - 11:20",
         5: "11:40 - 12:20",
         6: "12:35 - 13:15",
         7: "13:25 - 14:05",
         8: "14:15 - 14:55",}


def format_schedule(schedule: List[tuple]) -> str:
    res = []
    for lesson in schedule:
        number, lesson_name, room = lesson[1], lesson[3], lesson[4]
        res.append(f"{number} - {lesson_name}\n" + f"Кабинет {room}\n" + f"{bells[number]}")
    
    print("\n\n".join(res))
    return "\n\n".join(res)
            
    