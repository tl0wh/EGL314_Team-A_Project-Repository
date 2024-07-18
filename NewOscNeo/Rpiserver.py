from pythonosc import osc_server, dispatcher

# change the receiver_ip value to your RPi's IP address
receiver_ip = "192.168.1.100"
receiver_port = 2000

# this function prints the arguments in received OSC messages 
def print_args(addr, *args):
    if addr == "/print":
        print(args[0])

# this function executes received Python script
def execute_script(addr, script):
    try:
        exec(script)
    except Exception as e:
        print(f"Error executing script: {e}")

# catches OSC messages
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/print", print_args)  # if OSC message with addr "/print" is received, print_args function will run
dispatcher.map("/execute_script", execute_script)  # if OSC message with addr "/execute_script" is received, execute_script function will run

server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
print("serving on {}".format(server.server_address))
server.serve_forever()
