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
    -- Delete Screenshot
    -- os.remove(buff)

    local response = webclient:UploadData(url, "POST", Encoding.ASCII:GetBytes("process"))

    local FRAMES_TO_SKIP = 1
    -- Decode the response data and print it to the console
    local responseString = Encoding.ASCII:GetString(response)

    --randomness 
    local velocity = false;
    if (responseString ~= 'straight') then 
        local prob = math.random(1, 10) / 10
        print(prob)
        if (prob > 0.5) then
             velocity = true
        end
    end

    if ( responseString == 'straight' ) then 
        for i = 0, FRAMES_TO_SKIP, 1
        do
            joypad.set({B=true}, 1)
            emu.frameadvance()
        end
    elseif ( responseString == 'left' ) then 
        for i = 0, FRAMES_TO_SKIP, 1
        do
            if (velocity) then
                joypad.set({Left=true, B=true}, 1)
            else 
                joypad.set({Left=true, B=false}, 1)
            end
            emu.frameadvance()
        end
    elseif ( responseString == 'right' ) then 
        for i = 0, FRAMES_TO_SKIP, 1
        do
            if (velocity) then
                joypad.set({Right=true, B=true}, 1)
            else 
                joypad.set({Right=true, B=false}, 1)
            end
            emu.frameadvance()
        end
    end 
    print(responseString)
end