import scrapy

class EscolasGovSalvador(scrapy.Spider):
    name = 'escolas'

    urls = ['http://escolas.educacao.ba.gov.br/escolas?tipo=previous&tipo=next&js=1&field_municipio_value=1&form_build_id=form-3a0cfe4a1e0783dab8bf4708fc46baae&view_name=Escolas&view_display_id=page_1&view_path=escolas&view_base_path=escolas&view_dom_id=14850&pager_element=0&view_args=']

    def parse(self, response):
        import ipdb; ipdb.set_trace()
        pass
