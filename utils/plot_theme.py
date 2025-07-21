def apply_light_theme(fig):
    fig.update_layout(
        font=dict(color="black"),
        xaxis=dict(
            title_font=dict(color="black"),
            tickfont=dict(color="black")
        ),
        yaxis=dict(
            title_font=dict(color="black"),
            tickfont=dict(color="black")
        )
    )
    return fig
