$(document).ready(function () {
    // Toggle like button on click and update like count without reloading the page
    $("#like-form").submit(function (e) {
        e.preventDefault();
        const actionEndpoint = $(this).attr("action");
        const csrf_token = $(this).find("input[name='csrfmiddlewaretoken']").val();

        $.ajax({
            type: "POST",
            // url is the endpoint where the data will be processed.
            url: actionEndpoint,
            data: {
                'csrfmiddlewaretoken': csrf_token,
            },
            // dataType is the type of data you're expecting back from the server.
            dataType: "json",
            success: function (response) {
                // Update like count
                $("#like_count").text(response.like_count);
                // Toggle like button
                if (response.result === 'success') {
                    if (response.action === 'liked') {
                        $("button[name='blogpost_id']").html("<i class='fas fa-heart'></i>");
                    } else if (response.action === 'unliked') {
                        $("button[name='blogpost_id']").html("<i class='far fa-heart'></i>");
                    }
                } else {
                    console.error(response.message);
                }
            },
            error: function (response) {
                console.error("An error occurred while processing the form:");
                console.error(response);
            }
        });
    });
});