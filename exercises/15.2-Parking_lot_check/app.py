parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
slots=0
available=0
occupied=0
def get_parking_lot(parking):
    for row in parking:
        parkingStatus={}
        print(row)
        global slots,available,occupied
        slots=slots+(row.count(1)+row.count(2))
        occupied=occupied+row.count(1)
        available=available+row.count(2)
    parkingStatus.update({"total_slots":slots, "available_slots":available,"occupied_slots":occupied})
    return parkingStatus     
print(get_parking_lot(parking_state))
