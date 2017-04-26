from myutils import decode_message_type, decode_sub_type

class Message:
    ##
    # Message structure from: https://www.mysensors.org/download/serial_api_20#examples
    # node-id
    # ;child-sensor-id
    # ;message-type
    # ;ack
    # ;sub-type
    # ;payload
    # \n

    def __init__(self, sentence):
        (node_id,
         child_sensor_id,
         messsage_type,
         ack,
         sub_type,
         payload) = sentence.strip().split(';')

        self.node_id = int(node_id)
        self.child_sensor_id = int(child_sensor_id)
        self.message_type = decode_message_type(int(messsage_type))
        self.ack = ack
        self.sub_type = decode_sub_type(self.message_type, int(sub_type))
        self.payload = payload

    def decode_payload(self):
        print self.payload

    def __str__(self):
        return "node_id={self.node_id} child_sensor_id={self.child_sensor_id} message_type={self.message_type} ack={self.ack} sub_type={self.sub_type} payload={self.payload}".format(
                self=self)


def test_decode():
    m = Message("12;6;0;0;3;My Light")
    print m
    assert m.message_type == 'M_PRESENTATION'
    assert m.sub_type == "S_LIGHT"

    m = Message("12;6;1;0;0;36.5")
    print m
    assert m.message_type == 'M_SET'
    assert m.sub_type == "V_TEMP"

    m = Message("13;7;1;0;2;1")
    print m
    assert m.message_type == 'M_SET'
    assert m.sub_type == "V_LIGHT"
