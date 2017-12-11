def snowFlake(times,length=200.00):
    t.penUp()
    t.rotateTurtle(180)
    t.moveForward(300)
    t.rotateTurtle(-90)
    t.moveForward(170)
    t.rotateTurtle(-90)
    t.penDown()
    pattern = "MRMRM"
    for i in range(times):
        pattern =pattern.replace("M","MLMRMLM")
        for j in pattern:
            if j=="M":moveForward(length / (3.00 **(times - 1)))
            elif j=="L": t.rotateTurtle(60)
            elif j=="R": t.rotateTurtle(-120)
            t.rotateTurtle(-120)
            
