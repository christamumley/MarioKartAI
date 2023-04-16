luanet.load_assembly("System")
local WebClient = luanet.import_type("System.Net.WebClient")

local url = "http://localhost:8080" -- URL of the server to connect to

-- Create a new instance of the WebClient class and download the response from the server
local webclient = WebClient()
local response = webclient:DownloadString(url)

-- Print the response message
print(response)

client.screenshot("screenshot.png")
local response = webclient:UploadData(url, "POST", "image")

-- Decode the response data and print it to the console
local responseString = Encoding.ASCII:GetString(response)
print(responseString)