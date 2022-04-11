import math

class Check_Collision:
    def check_two_rectangles_collision(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
        return r1x + r1w > r2x and r1x < r2x + r2w and r1y + r1h > r2y and r1y < r2y + r2h

    def collision_rectangle_circle(rleft, rtop, width, height,
                                   center_x, center_y, radius):

        rright, rbottom = rleft + width/2, rtop + height/2
        cleft, ctop = center_x-radius, center_y-radius
        cright, cbottom = center_x+radius, center_y+radius

        if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
            return False

        for x in (rleft, rleft+width):
            for y in (rtop, rtop+height):
                if math.hypot(x-center_x, y-center_y) < radius:
                    return True

        if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
            return True

        return False