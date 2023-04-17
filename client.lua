luanet.load_assembly("System")
local WebClient = luanet.import_type("System.Net.WebClient")
local Encoding = luanet.import_type("System.Text.Encoding")

local url = "http://localhost:8080" -- URL of the server to connect to

-- Create a new instance of the WebClient class and download the response from the server
local webclient = WebClient()
local response = webclient:DownloadString(url)

while true do
    local headers = {} -- Optional headers to include in the request

    -- Pack the image into a request 
    local buff = "./buff.png"
    client.screenshot(buff)
    local file = io.open(buff, "rb")
    local data = file:read("*all")
    file:close()
    -- Delete Screenshot
    --os.remove(buff)


    webclient.Headers:Add("Content-Type", "image/png")
    local response = webclient:UploadData(url, "POST", data)

    local FRAMES_TO_SKIP = 24
    -- Decode the response data and print it to the console
    local responseString = Encoding.ASCII:GetString(response)
    if ( responseString == 'straight' ) then 
        for i = 0, FRAMES_TO_SKIP, 1
        do
            joypad.set({B=true}, 1)
            emu.frameadvance()
        end
    elseif ( responseString == 'left' ) then 
        for i = 0, FRAMES_TO_SKIP, 1
        do
            joypad.set({Left=true, B=true}, 1)
            emu.frameadvance()
        end
    elseif ( responseString == 'right' ) then 
        for i = 0, FRAMES_TO_SKIP, 1
        do
            joypad.set({Right=true, B=true}, 1)
            emu.frameadvance()
        end
    end 
    print(responseString)

    -- local FRAMES_TO_SKIP = 24
    -- for i = 0, FRAMES_TO_SKIP, 1
    -- do
    --     emu.frameadvance()
    -- end
end