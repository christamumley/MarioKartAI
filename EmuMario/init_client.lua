luanet.load_assembly("System")
local WebClient = luanet.import_type("System.Net.WebClient")
local Encoding = luanet.import_type("System.Text.Encoding")

local url = "http://localhost:8080" -- URL of the server to connect to

-- Create a new instance of the WebClient class and download the response from the server
local webclient = WebClient()
local response = webclient:DownloadString(url)

local data = "name=John&age=30" -- The data to send in the request body
local headers = {} -- Optional headers to include in the request

for key, value in pairs(headers) do
    webclient.Headers:Add(key, value)
end

-- Print the response message
print(response)

client.screenshot("screenshot.png")

-- Convert the data to a byte array and send the POST request
local bytes = Encoding.ASCII:GetBytes(data)
local response = webclient:UploadData(url, "POST", bytes)

-- Decode the response data and print it to the console
local responseString = Encoding.ASCII:GetString(response)
print(responseString)