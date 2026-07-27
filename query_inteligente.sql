WITH tb_compras AS(
    SELECT dt_compra,
        produto,
        avg(valor_produto) as valor_produto
    FROM compras
    GROUP BY dt_compra,
        produto
),
TB_LAG AS(
    SELECT *,
        LAG(dt_compra) OVER(
            PARTITION BY produto
            ORDER BY dt_compra
        ) AS dt_compra_anterior
    FROM tb_compras
    ORDER BY produto,
        dt_compra
),
tb_avg AS(
    SELECT produto,
        avg(
            julianday(dt_compra) - julianday(dt_compra_anterior)
        ) AS avg_diff_dias_entre_compras
    FROM TB_LAG
    GROUP BY produto
),
TB_STATS_PRODUTO AS (
    SELECT produto,
        max(dt_compra) AS dt_ultima_compra,
        avg(valor_produto) AS media_valor_produto
    FROM compras
    GROUP BY produto
),
tb_final AS(
    SELECT T1.*,
        T2.avg_diff_dias_entre_compras,
        julianday('now') - julianday(dt_ultima_compra) as dias_desde_ultima_compra
    FROM TB_STATS_PRODUTO as T1
        LEFT JOIN tb_avg as T2 ON T1.produto = T2.produto
)
SELECT *
FROM tb_final
ORDER BY dt_ultima_compra