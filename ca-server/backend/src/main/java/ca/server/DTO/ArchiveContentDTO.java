package ca.server.DTO;

import lombok.Data;

import java.math.BigDecimal;

@Data
public class ArchiveContentDTO {
    private Integer id;

    private Integer cik;

    private Integer year;

    private BigDecimal earningsPerShare;

    private String stateCountry;

    private String office;

    private String company;
}
