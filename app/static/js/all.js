$(".order-btn").on("click", function (e) {
    const orderField = $(this).data("order");

    $.ajax({
        url: SUBJECTS_API_URL,
        type: "GET",
        data: {
            ordering: orderField ? orderField : "id"
        },
        success: function (data) {
            window.location.href = `${SUBJECTS_API_URL}?ordering=${orderField}`;
        }
    });
});