import win32ui
import dde

server = dde.CreateServer()
server.Create("TestClient") # This can be anything or even empty.
conversation = dde.CreateConversation(server)
conversation.ConnectTo("telem", "Anything") # MoTeC DDE application is "telem", yours can be anything.
