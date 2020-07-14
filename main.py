import pygame



focus = None

#initilization
pygame.init()

#making a key for keys
keyKey = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')


#hourly price
cost = 2.50

totalCost = 0

cost_output = ''
cost_pos = (0,0)


#making the window
scr_width = 1200
scr_height = 800

win = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Parking Machine")


##adding button onclick event
def checkPrice():
    global cost
    global totalCost
    global cost_output
    global cost_pos

    length = hours.get()

    try:
        totalCost = float(length) * float(cost)
    except ValueError:
        return

    totalCost = ("£{}0".format(str(totalCost)))


    ###printing output to the screen
    priceOutput.pos = (submit.pos[0], submit.pos[1] + 2 * submit.WH[1])

    priceOutput.text = "total cost for {} is {}".format(str(reg.get()), totalCost)

    ###saving to log
    log = open('records.txt', 'a')


    

    log.write("\nreg: {} \n price payed: {}\n\n".format(str(reg.get()), str(totalCost) ))

    log.close()










###text box
class textbox():

    def __init__(self, font, size, location, limit, hint):
        self.content = []
        self.font = pygame.font.Font(font, size)
        self.pos = location
        self.limit = limit
        self.hint = hint

        self.focus = False

        ###drawing box around the area
        global scr_width; global scr_height

        self.box_limit = (scr_width - 2 * location[0], int(size / 2 + 15))


    def addChar(self, char):
        char = str(char)
        #checking that only a single char has been inputed, some emojis wont work oh well :-(
        if len(char) > 1:
            return
        #checking limit
        elif len(self.content) > self.limit:
            return
        else:
            self.content.append(char)

    #deleting chars after backspace
    def remChar(self):
        if len(self.content) > 0:
            del(self.content[-1])

    #rendering to screen
    def render(self):
        #outline colour depending on focus
        if self.focus:
            colour = (0,0,0)
        else:
            colour = (130,130,130)
        #outline
        pygame.draw.rect(win, colour, (self.pos[0], self.pos[1], self.box_limit[0], self.box_limit[1]), 3)


        if len(self.content) > 0:
            output = self.font.render(''.join(self.content), True, (0,0,0))
        else:
            output = self.font.render(self.hint, True, (200,200,200))


        win.blit(output, self.pos)




    #function to get the data from a text box
    def get(self):
        return ''.join(self.content)


    #function to check if text box should be in foucs
    def checkFocus(self):
        global focus

        mouse_pos = pygame.mouse.get_pos()

        #check if mouse is in box limit
        if int(mouse_pos[0]) > int(self.pos[0]) and int(mouse_pos[0]) < int(self.box_limit[0] + self.pos[0]) and int(mouse_pos[1]) > int(self.pos[1]) and int(mouse_pos[1]) < int(self.box_limit[1] + self.pos[1]):
            self.focus = True
            focus = self
        else:
            self.focus = False

            #checking if this box was previously in focus
            if focus == self:
                focus = None



#####function for a button
class button():

    def __init__(self, pos, widthHeight, colour, highlight, text, font, size, exec):
        self.pos = pos
        self.WH = widthHeight
        self.prim_colour = colour
        self.highlight = highlight
        self.text = text
        self.execute = exec
        self.colour = self.prim_colour
        self.font = pygame.font.Font(font, size)

        self.hover = False

    def checkHighlight(self):
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pos[0] > self.pos[0] and mouse_pos[0] < self.pos[0] + self.WH[0]    and    mouse_pos[1] > self.pos[1] and mouse_pos[1] < self.pos[1] + self.WH[1]:
            self.colour = self.highlight
            self.hover = True
        else:
            self.colour = self.prim_colour
            self.hover = False


    def render(self):
        pygame.draw.rect(win, self.colour, (self.pos[0], self.pos[1], self.WH[0], self.WH[1]))

        #text handeling
        output = self.font.render(self.text, True, (0,0,0))
        win.blit(output, (self.pos[0], int(self.WH[1]/3) + self.pos[1]))

    def checkSelect(self):
        if self.hover:
            self.execute()

class label():

    def __init__(self, pos, text, font, size):
        self.pos = pos
        self.text = text
        self.font = pygame.font.Font(font, size)

    def render(self):

        output = self.font.render(self.text, True, (0,0,0))
        win.blit(output, self.pos)










#####Making objects
reg = textbox(None, 72, (int(100),int(100)), 10, "Please enter car registration")
hours = textbox(None, 72, (int(100),int(170)), 1, "How many hours do you wish to stay?")

submit = button((100, 300), (200, 100), (0,0,255), (255,0,255), "Continue", None, 56, checkPrice)

priceOutput = label(cost_pos, '', None, 60)





#####Loop
run = True
while run:

    ###event handeling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            #establishing if key is a letter
            if event.key < 123 and event.key > 96:
                #making the aplhabet 0-25 to be compared to keykey
                keyPressed = event.key - 97

                ###outputting text
                try:
                    focus.addChar(keyKey[keyPressed])
                except:
                    pass

            #etsblishing if key is a number
            elif event.key > 47 and event.key < 58:

                keyPressed = event.key - 48
                focus.addChar(str(keyPressed))

            #backspace
            elif event.key == pygame.K_BACKSPACE:
                focus.remChar()

            #space
            elif event.key == pygame.K_SPACE:
                focus.addChar(' ')

        ##clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            reg.checkFocus()
            hours.checkFocus()
            submit.checkSelect()





    ####rendering
    reg.render()
    hours.render()

    submit.checkHighlight()
    submit.render()

    priceOutput.render()







    #### updating
    pygame.time.delay(10)
    pygame.display.update()
    win.fill((255,255,255))


#### Tidying up
pygame.quit()
quit()
