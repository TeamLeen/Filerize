// TODO: allow to edit the folder
async function display_folders(){
    let config_request = await eel.get_config_file_content();
    let config = await config_request();
    let folders = config["folders"];
    $("#folders_list").html(
        `
            ${folders.map(
                folder => `
                    <div class='folders has-background-white rounded py-5 px-5 mb-4'>
                        <div class='columns'>
                            <div class='column'>
                                <span class='fw-bold has-text-weight-bold'>Path:</span> <span class='path_display'>${folder.path}</span>
                            </div>
                            <div>
                                <button class='button is-danger is-small mr-2 rounded delete_button'>
                                    X
                                </button>
                            </div>
                        </div>

                        <div>
                            <span class='fw-bold has-text-weight-bold'>Summary:</span>
                            ${folder.summary}
                        </div>
                        
                    </div>
                `
            ).join("")}   
        `
    )
}

$(".folder_select").click(async e => {
    let request = await eel.choose_folder()
    let value = await request();

    let path_element =  $(e.target).find(".path");
    if (path_element.length == 0){
        path_element = $(e.target).siblings(".path");
    }
    path_element.text(value);
});


$("#new_folder_form").submit(async (e) => {
    e.preventDefault();
    let folder_path = $("#new_folder_form").find(".path").text();
    let folder_description = $("#new_folder_form").find("#folder_description").val();

    if(folder_path == ""){
        alert("Please select a folder");
        return;
    }

    if(folder_description == ""){
        alert("Please write a description");
        return;
    }

    let config_request = await eel.get_config_file_content();
    let config = await config_request();
    let folders = config["folders"]; 
    
    // Ensure that there is no folders with the same paths
    for (let i = 0; i < folders.length; i++){
        let folder = folders[i];
        if(folder.path == folder_path){
            alert("Folder already exists");
            return;
        }
    }

    await eel.add_new_folder(folder_path, folder_description);
    $("#new_folder_form").find(".path").text("");
    $("#new_folder_form").find("#folder_description").val("");

    display_folders();
});

$(document).on("click", ".delete_button", async function(){
    let sure = confirm("Are you sure?");
    if(sure){
        let folder_path = $(this).parent().parent().find(".path_display").text();
        await eel.delete_folder(folder_path);
        display_folders(); 
    }
});


$(document).ready(function(){
    display_folders();
});