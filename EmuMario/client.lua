luanet.load_assembly("System")
local WebClient = luanet.import_type("System.Net.WebClient")
local Encoding = luanet.import_type("System.Text.Encoding")

local url = "http://localhost:8080" -- URL of the server to connect to

-- Create a new instance of the WebClient class and download the response from the server
local webclient = WebClient()
local response = webclient:DownloadString(url)

local headers = {} -- Optional headers to include in the request

for key, value in pairs(headers) do
    webclient.Headers:Add(key, value)
end

-- Print the response message
print(response)

-- Pack the image into a request 
local buff = "./buff.png"
client.screenshot(buff)
local file = io.open(buff, "rb")
local data = file:read("*all")
file:close()
-- Delete Screenshot
os.remove(buff)

-- Convert the data to a byte array and send the POST request
-- local bytes = Encoding.ASCII:GetBytes(file)
webclient.Headers:Add("Content-Type", "image/png")
local response = webclient:UploadData(url, "POST", data)

-- Decode the response data and print it to the console
local responseString = Encoding.ASCII:GetString(response)
if ( responseString == 'Right' )
then 
    gui.text(50, 50, 'Right Pressed.')
    while true do
        joypad.set({Right=true, B=true}, 1)
        emu.frameadvance()
    end
end 
print(responseString)