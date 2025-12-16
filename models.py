"""
SQLAlchemy ORM Models for the database
Auto-generated - DO NOT EDIT MANUALLY
Run generate_models.py to regenerate
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Numeric, Text, Boolean, MetaData, Table, inspect, BigInteger, SmallInteger, Date, Time, Float, LargeBinary, JSON, text
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus
from config import DB_CONFIG
from datetime import datetime

# URL encode password to handle special characters like @
encoded_password = quote_plus(DB_CONFIG['password'])

# Create database connection string
DATABASE_URL = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{encoded_password}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

# Create engine
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


class ShippingRates(Base):
    __tablename__ = 'Shipping_rates'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(String(255), nullable=True)
    supplier_name = Column(String(255), nullable=True)
    minimum_we = Column(Float, nullable=True)
    weight_increment = Column(String(255), nullable=True)
    shipment_zone = Column(String(255), nullable=True)
    Forward_first_slab_cost = Column(String(255), nullable=True)
    Forward_incremental_cost = Column(String(255), nullable=True)
    rto_first_slab_cost = Column(String(255), nullable=True)
    rto_incremental_cost = Column(String(255), nullable=True)
    dto_first_slab_cost = Column(String(255), nullable=True)
    dto_incremental_cost = Column(String(255), nullable=True)
    FSC_cost = Column(String(255), nullable=True)
    QC_charges = Column(String(255), nullable=True)
    min_cod_charge = Column(String(255), nullable=True)
    cod_charge_rate = Column(String(255), nullable=True)
    date_from = Column(Time, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class AccountingTypes(Base):
    __tablename__ = 'accounting_types'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounting_type = Column(String(20), nullable=True)

class AdditionalEmails(Base):
    __tablename__ = 'additional_emails'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    email = Column(String(80), nullable=False)
    type = Column(String(255), nullable=True)
    is_active = Column(SmallInteger, nullable=True, server_default='1')
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class AdvancedPartnerPreferenceSettings(Base):
    __tablename__ = 'advanced_partner_preference_settings'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    redis_key = Column(String(100), nullable=False)
    service_type = Column(String(255), nullable=False)
    settings = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class AirDomCosting(Base):
    __tablename__ = 'air_dom_costing'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    costing_logic = Column(String(255), nullable=False)
    per_slab_cost = Column(Text, nullable=False)
    service_tax = Column(Float, nullable=True)
    fuel_surcharge = Column(Float, nullable=False)
    cod_tax = Column(String(100), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    from_date = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    classes = Column(Text, nullable=False)
    extra_charges = Column(Text, nullable=False)
    volumetric_formula = Column(String(255), nullable=False)
    accounts_entity_id = Column(Integer, nullable=True)
    is_reverse = Column(SmallInteger, nullable=False, server_default='0')
    is_rto = Column(SmallInteger, nullable=False, server_default='0')

class AirDomRates(Base):
    __tablename__ = 'air_dom_rates'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=False, server_default='0')
    durations = Column(Text, nullable=False)
    has_cod = Column(SmallInteger, nullable=False)
    has_express = Column(SmallInteger, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    has_cash = Column(SmallInteger, nullable=False)
    has_repl = Column(SmallInteger, nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    region = Column(String(100), nullable=False)
    from_date = Column(DateTime, nullable=True)
    is_stressed = Column(SmallInteger, nullable=False, server_default='0')

class AirDomesticModes(Base):
    __tablename__ = 'air_domestic_modes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    mode_type = Column(String(20), nullable=True)

class AirDomesticNddCosting(Base):
    __tablename__ = 'air_domestic_ndd_costing'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=True)
    supplier_id = Column(Integer, nullable=False)
    costing_logic = Column(String(255), nullable=False)
    per_slab_cost = Column(Text, nullable=False)
    fuel_surcharge = Column(Float, nullable=False)
    cod_tax = Column(String(100), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    from_date = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    classes = Column(Text, nullable=False)
    extra_charges = Column(Text, nullable=False)
    volumetric_formula = Column(String(255), nullable=False)
    is_reverse = Column(SmallInteger, nullable=False, server_default='0')
    is_rto = Column(SmallInteger, nullable=False, server_default='0')

class AirDomesticNddPincodes(Base):
    __tablename__ = 'air_domestic_ndd_pincodes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=False, server_default='0')
    durations = Column(Text, nullable=False)
    has_cod = Column(SmallInteger, nullable=False)
    has_express = Column(SmallInteger, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    has_cash = Column(SmallInteger, nullable=False)
    has_repl = Column(SmallInteger, nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    region = Column(String(100), nullable=False)

class AirInternationalPricing(Base):
    __tablename__ = 'air_international_pricing'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    city_id = Column(Integer, nullable=False)
    supplier_id = Column(Integer, nullable=False)
    accounts_entity_id = Column(Integer, nullable=True)
    from_date = Column(DateTime, nullable=True)
    slabs = Column(Text, nullable=False)
    surcharges = Column(Text, nullable=False)
    durations = Column(Text, nullable=False)
    shipment_type = Column(String(20), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class AirIntlCountry(Base):
    __tablename__ = 'air_intl_country'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    country = Column(String(100), nullable=False)
    lcase_name = Column(String(100), nullable=False)
    is_active = Column(SmallInteger, nullable=False, server_default='1')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    abbr = Column(String(3), nullable=False)

class AirIntlSource(Base):
    __tablename__ = 'air_intl_source'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    is_active = Column(SmallInteger, nullable=False, server_default='1')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class AirtableMof(Base):
    __tablename__ = 'airtable_mof'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    record_id = Column(String(100), nullable=True)
    shipment_no = Column(BigInteger, nullable=True)
    vs_notes = Column(Text, nullable=True)
    awb = Column(String(20), nullable=True)
    manual_case = Column(String(50), nullable=True)
    partner_remarks = Column(Text, nullable=True)
    partner_name = Column(String(50), nullable=True)
    consignee_name = Column(String(100), nullable=True)
    vamashipper = Column(String(50), nullable=True)
    consignee_no = Column(String(20), nullable=True)
    source_of_complaint = Column(String(50), nullable=True)
    latest_tracking_status = Column(String(50), nullable=True)
    email_subject = Column(Text, nullable=True)
    shipment_booking_date = Column(Date, nullable=True)
    auto_ticket_status = Column(String(20), nullable=True)
    manual_ticket_status = Column(String(20), nullable=True)
    closure_date = Column(DateTime, nullable=True)
    created_on = Column(String(100), nullable=True)
    ticket_delay = Column(Integer, nullable=True)
    updated_at_airtable = Column(String(100), nullable=True)
    trim_awb = Column(String(20), nullable=True)
    duplicate_awb = Column(Integer, nullable=True)
    calculation = Column(Integer, nullable=True)
    last_modified_by = Column(String(100), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class AllIndiaPincodes(Base):
    __tablename__ = 'all_india_pincodes'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    pincode = Column(String(20), nullable=True)
    area = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    latitude = Column(String(20), nullable=False)
    longitude = Column(String(20), nullable=False)
    state_code = Column(String(3), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class AmazonShipmentAdditionalDetails(Base):
    __tablename__ = 'amazon_shipment_additional_details'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(String(200), nullable=False)
    amazon_shipment_no = Column(String(200), nullable=True)
    carrier_id = Column(String(200), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)

class AmbassadorClientsMappings(Base):
    __tablename__ = 'ambassador_clients_mappings'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ambassador_id = Column(BigInteger, nullable=False)
    accounts_entity_id = Column(BigInteger, nullable=False)
    accounts_user_id = Column(BigInteger, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class AmbassadorCreditTransactionMappings(Base):
    __tablename__ = 'ambassador_credit_transaction_mappings'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    ambassador_id = Column(BigInteger, nullable=False)
    transaction_id = Column(BigInteger, nullable=False)
    vama_transaction_id = Column(BigInteger, nullable=False)
    transaction_reference_number = Column(String(150), nullable=False)
    transaction_amount = Column(Numeric(20,  2), nullable=False)
    quick_books_id = Column(String(20), nullable=True)

class AmbassadorInvites(Base):
    __tablename__ = 'ambassador_invites'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    ambassador_id = Column(BigInteger, nullable=False)
    email = Column(String(150), nullable=False)
    invite_date = Column(Date, nullable=False)
    invite_expiration_date = Column(Date, nullable=False)

class AmbassadorPricing(Base):
    __tablename__ = 'ambassador_pricing'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    ambassador_id = Column(BigInteger, nullable=False)
    service_type = Column(String(150), nullable=True)
    supplier_id = Column(BigInteger, nullable=False)
    is_reverse = Column(SmallInteger, nullable=False, server_default='0')
    rates = Column(Text, nullable=True)
    applicable_from = Column(DateTime, nullable=True)

class Ambassadors(Base):
    __tablename__ = 'ambassadors'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=True)
    email = Column(String(80), nullable=False)
    password = Column(String(255), nullable=False)
    clients = Column(Text, nullable=False)
    active = Column(SmallInteger, nullable=False)
    total_amount = Column(Text, nullable=False)
    total_shipments = Column(Text, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    total_cod_shipments = Column(Text, nullable=False)
    sign_up_url = Column(Text, nullable=False)
    first_name = Column(String(80), nullable=True)
    last_name = Column(String(80), nullable=True)
    future_prospects = Column(String(150), nullable=True)
    mobile_number = Column(String(20), nullable=True)
    api_key = Column(String(100), nullable=True)
    reward_type = Column(String(255), nullable=False)
    deleted_at = Column(Time, nullable=True)
    is_admin = Column(SmallInteger, nullable=True, server_default='0')

class Announcements(Base):
    __tablename__ = 'announcements'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    notification_text = Column(Text, nullable=False)
    expire_at = Column(DateTime, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class AwbCategories(Base):
    __tablename__ = 'awb_categories'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    category_name = Column(String(20), nullable=True)

class B2cSwitchedShipments(Base):
    __tablename__ = 'b2c_switched_shipments'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    tracking_id = Column(String(20), nullable=False)
    supplier_id = Column(Integer, nullable=False)
    original_supplier_id = Column(Integer, nullable=True)

class BookingLaps(Base):
    __tablename__ = 'booking_laps'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    validation_started_at = Column(DateTime, nullable=True)
    validation_ended_at = Column(DateTime, nullable=True)
    quoting_started_at = Column(DateTime, nullable=True)
    quoting_ended_at = Column(DateTime, nullable=True)
    ordering_started_at = Column(DateTime, nullable=True)
    ordering_ended_at = Column(DateTime, nullable=True)
    shipment_creation_started_at = Column(DateTime, nullable=True)
    shipment_creation_ended_at = Column(DateTime, nullable=True)
    booking_started_at = Column(DateTime, nullable=True)
    booking_ended_at = Column(DateTime, nullable=True)

class BookingLogs(Base):
    __tablename__ = 'booking_logs'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    supplier_id = Column(BigInteger, nullable=False)
    request = Column(Text, nullable=True)
    response = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))

class CallingResults(Base):
    __tablename__ = 'calling_results'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ref_no = Column(BigInteger, nullable=True)
    calling_timestamp = Column(DateTime, nullable=True)
    calling_type = Column(SmallInteger, nullable=True)
    calling_status = Column(SmallInteger, nullable=True)
    accounts_entity_id = Column(Integer, nullable=False)
    futwork_unique_id = Column(String(255), nullable=True)
    comment = Column(String(255), nullable=True)
    call_outcome = Column(SmallInteger, nullable=True)
    uploaded_by = Column(String(255), nullable=True)
    link = Column(String(512), nullable=True)
    created_at_ist = Column(Time, nullable=False, server_default=text('current_timestamp()'))

class CancellationLogs(Base):
    __tablename__ = 'cancellation_logs'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    accounts_user_id = Column(String(30), nullable=True)
    created_at = Column(Time, nullable=False)
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    request = Column(Text, nullable=True)
    response = Column(Text, nullable=True)

class ChannelFulfillment(Base):
    __tablename__ = 'channel_fulfillment'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    channel_name = Column(String(20), nullable=False)
    channel_order_id = Column(String(50), nullable=True)
    channel_fulfillment_id = Column(String(50), nullable=True)
    tracking_id = Column(String(50), nullable=True)
    tracking_company = Column(String(100), nullable=True)
    location_id = Column(String(20), nullable=True)
    status = Column(String(50), nullable=False)
    fulfilled_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    last_update_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    tracking_url = Column(Text, nullable=True)
    channel_fulfillment_meta = Column(Text, nullable=False)
    channel_fulfillment_extra = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)

class ChannelMasters(Base):
    __tablename__ = 'channel_masters'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    channel_code = Column(String(10), nullable=False)
    channel_name = Column(String(100), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class ChannelOrderMeta(Base):
    __tablename__ = 'channel_order_meta'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    order_id = Column(Integer, nullable=False)
    order_meta = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)

class ChannelWebhooks(Base):
    __tablename__ = 'channel_webhooks'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=False)
    channel_unique_id = Column(String(50), nullable=True)
    channel_mapping_id = Column(Integer, nullable=False)
    channel_id = Column(String(10), nullable=False)
    channel_name = Column(String(50), nullable=False)
    webhook_id = Column(String(50), nullable=True)
    type = Column(String(50), nullable=True)
    format = Column(String(50), nullable=True)
    api_version = Column(String(50), nullable=True)
    url = Column(String(200), nullable=True)
    webhook_meta = Column(Text, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    updated_at = Column(Time, nullable=False)
    deleted_at = Column(Time, nullable=True)

class ChargeHeads(Base):
    __tablename__ = 'charge_heads'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    service_id = Column(Integer, nullable=False)
    head_name = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    unique_name = Column(String(255), nullable=False)
    service_accounting_code = Column(String(255), nullable=False)
    service_type = Column(String(255), nullable=False)
    exempted = Column(SmallInteger, nullable=False, server_default='0')
    gst = Column(Numeric(5,  2), nullable=False)
    igst = Column(Numeric(5,  2), nullable=False)
    cgst = Column(Numeric(5,  2), nullable=False)
    sgst = Column(Numeric(5,  2), nullable=False)
    status = Column(SmallInteger, nullable=False)
    quick_books_id = Column(BigInteger, nullable=False, server_default='0')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class ChildAwbNumbers(Base):
    __tablename__ = 'child_awb_numbers'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    supplier_id = Column(Integer, nullable=False)
    child_awb_number = Column(String(100), nullable=False)

class CityPairsAndDistances(Base):
    __tablename__ = 'city_pairs_and_distances'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    city_name_1 = Column(String(255), nullable=False)
    city_name_2 = Column(String(255), nullable=False)
    distance_kms = Column(String(20), nullable=False)
    supplier_id = Column(Integer, nullable=False)
    city_name_1_aliases = Column(Text, nullable=True)
    city_name_2_aliases = Column(Text, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    updated_at = Column(Time, nullable=False)

class CodTransactions(Base):
    __tablename__ = 'cod_transactions'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_user_id = Column(BigInteger, nullable=False)
    accounts_entity_id = Column(BigInteger, nullable=False)
    cod_ref_no = Column(BigInteger, nullable=False)
    shipment_no = Column(BigInteger, nullable=True)
    awb_no = Column(String(255), nullable=True)
    shipment_date = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    cod_amount = Column(Numeric(20,  2), nullable=True)
    supplier_id = Column(BigInteger, nullable=False)
    status = Column(SmallInteger, nullable=False)
    instant_cod_status = Column(SmallInteger, nullable=True, server_default='0')
    delivered_date = Column(DateTime, nullable=True)
    cod_collection_ref_no = Column(String(100), nullable=True)
    cod_collected = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    cod_collection_pending = Column(Numeric(20,  2), nullable=True)
    cod_collection_date = Column(DateTime, nullable=True)
    payment_mode = Column(String(255), nullable=True)
    payment_ref_no = Column(String(255), nullable=True)
    transaction_type = Column(String(150), nullable=True)
    paid_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    pending_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    payment_date = Column(DateTime, nullable=True)
    remittance_upload_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)
    converted_at = Column(DateTime, nullable=True)
    initiated_at = Column(DateTime, nullable=True)
    remittance_batch_id = Column(BigInteger, nullable=True)
    remitted_by = Column(Integer, nullable=True)

class CountriesMaster(Base):
    __tablename__ = 'countries_master'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    isd_code = Column(String(255), nullable=False)
    two_digit_code = Column(String(255), nullable=False)
    three_digit_code = Column(String(255), nullable=False)
    created_at = Column(Time, nullable=True)
    updated_at = Column(Time, nullable=True)

class CustomerApiCallbackLog(Base):
    __tablename__ = 'customer_api_callback_log'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    response = Column(Text, nullable=True)
    accounts_entity_id = Column(BigInteger, nullable=True)
    callback_type = Column(String(200), nullable=False)
    callback_url = Column(String(500), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class CustomerPricingPlans(Base):
    __tablename__ = 'customer_pricing_plans'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    pricing_plan_id = Column(Integer, nullable=False)
    accounts_entity_id = Column(BigInteger, nullable=True)
    from_date = Column(DateTime, nullable=False)
    creator = Column(Integer, nullable=False)
    to_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False)

class DisputedShipments(Base):
    __tablename__ = 'disputed_shipments'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    supplier_id = Column(Integer, nullable=False)
    accounts_entity_id = Column(Integer, nullable=False)
    booked_weight = Column(Numeric(20,  2), nullable=True)
    changed_weight = Column(Numeric(20,  2), nullable=True)
    settled_weight = Column(Numeric(20,  2), nullable=True)
    weight_amount = Column(Numeric(20,  2), nullable=True)
    weight_uploaded_by = Column(Integer, nullable=True)
    status = Column(SmallInteger, nullable=True)
    dimentions = Column(String(100), nullable=True)
    product_name = Column(String(250), nullable=True)
    rejection_reasons = Column(String(250), nullable=True)
    booked_at = Column(Time, nullable=True)
    changed_at = Column(Time, nullable=True)
    raised_at = Column(Time, nullable=True)
    settled_at = Column(Time, nullable=True)
    settled_in_days = Column(Numeric(20,  2), nullable=True)
    created_at = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True)
    deleted_at = Column(Time, nullable=True)

class DoctrineMigrationVersions(Base):
    __tablename__ = 'doctrine_migration_versions'

    version = Column(String(191), primary_key=True, nullable=False)
    executed_at = Column(DateTime, nullable=True)
    execution_time = Column(Integer, nullable=True)

class DomesticPincodeMasters(Base):
    __tablename__ = 'domestic_pincode_masters'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    pincode = Column(String(8), nullable=False)
    city = Column(String(200), nullable=False)
    state = Column(String(200), nullable=False)
    region = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class Ecom2Transactions(Base):
    __tablename__ = 'ecom2_transactions'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    vama_transaction_id = Column(BigInteger, nullable=False)
    sac = Column(BigInteger, nullable=True)
    voucher_no = Column(String(30), nullable=True)
    order_id = Column(BigInteger, nullable=False)
    user_id = Column(BigInteger, nullable=False)
    payment_mode = Column(String(100), nullable=True)
    payment_type = Column(String(20), nullable=True)
    accounting_type = Column(String(255), nullable=True)
    transaction_data = Column(Text, nullable=True)
    transaction_amount = Column(Numeric(20,  2), nullable=False)
    transaction_unique_id = Column(String(100), nullable=True)
    transaction_by = Column(BigInteger, nullable=False)
    remark = Column(Text, nullable=False)
    invoice_no = Column(String(50), nullable=True)
    quick_books_id = Column(String(20), nullable=True)
    qb_transaction_id = Column(String(50), nullable=True)
    qb_payment_id = Column(String(50), nullable=True)
    status = Column(SmallInteger, nullable=False, server_default='0')
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)
    request_parameters = Column(Text, nullable=False)
    gateway_name = Column(String(255), nullable=False)
    payment_request_token = Column(String(255), nullable=False)
    payment_api_response = Column(Text, nullable=False)
    payment_status = Column(String(255), nullable=False)
    reference_table = Column(String(255), nullable=False)
    reference_id = Column(String(255), nullable=True)
    master_user_id = Column(Integer, nullable=False)
    received_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    credit_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    debit_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    transaction_status = Column(SmallInteger, nullable=True, server_default='0')

class Ecom3SuccessfulSynchronisations(Base):
    __tablename__ = 'ecom3_successful_synchronisations'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    table_name = Column(String(100), nullable=False)
    ecom2_last_inserted_id = Column(Integer, nullable=False)

class EmailLogs(Base):
    __tablename__ = 'email_logs'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    recipients = Column(Text, nullable=False)
    sender = Column(Text, nullable=False)
    email_subject = Column(String(500), nullable=False)
    status = Column(Text, nullable=False)
    delivery_report_response = Column(Text, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class EmployeeDashboardMappings(Base):
    __tablename__ = 'employee_dashboard_mappings'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dashboard_id = Column(Integer, nullable=False)
    role_id = Column(String(255), nullable=True)
    employee_id = Column(Integer, nullable=True)
    department_code = Column(String(255), nullable=True)
    designation_code = Column(String(255), nullable=True)
    created_at = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class EmployeeDepartmentAndDesignationMappings(Base):
    __tablename__ = 'employee_department_and_designation_mappings'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    department_code = Column(String(255), nullable=False)
    designation_code = Column(String(255), nullable=False)
    created_at = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class EmployeeDepartments(Base):
    __tablename__ = 'employee_departments'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    code = Column(String(255), nullable=False)
    department_name = Column(String(255), nullable=False)
    created_at = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class EmployeePermissionMaster(Base):
    __tablename__ = 'employee_permission_master'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    permissions = Column(Text, nullable=False)
    created_at = Column(Time, nullable=False)
    updated_at = Column(Time, nullable=True)
    deleted_at = Column(Time, nullable=True)

class EmployeeRoles(Base):
    __tablename__ = 'employee_roles'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    role_name = Column(String(255), nullable=False)
    role_setting = Column(Text, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class Employees(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=True)
    role_id = Column(Integer, nullable=True)
    deactivated_on = Column(Time, nullable=True)
    email = Column(String(50), nullable=False)
    password = Column(String(255), nullable=True)
    mobile_no = Column(String(255), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)

class Entities(Base):
    __tablename__ = 'entities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=True)
    entity_name = Column(String(150), nullable=False)
    instant_cod_day = Column(Integer, nullable=True)
    slug = Column(String(100), nullable=True)
    logo = Column(String(100), nullable=True)
    sameday_cod = Column(SmallInteger, nullable=False, server_default='0')
    credit_limit = Column(Numeric(10,  2), nullable=False, server_default='0.00')
    credit_balance = Column(Numeric(12,  2), nullable=True)
    qb_outstanding = Column(BigInteger, nullable=True, server_default='0')
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    minimum_balance_amount = Column(Integer, nullable=True, server_default='1000')
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)
    credit_period = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    sales_person_id = Column(Integer, nullable=True)
    spoc_person_id2 = Column(BigInteger, nullable=True)
    spoc_second_person_id = Column(Integer, nullable=True)
    spoc_person_id = Column(BigInteger, nullable=True)
    cod_adjustable = Column(SmallInteger, nullable=True, server_default='0')
    instant_cod_enabled = Column(SmallInteger, nullable=True, server_default='0')
    entity_classification_status = Column(String(255), nullable=True)
    created_at_ist = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    website_link = Column(String(500), nullable=True)
    acquisition_source = Column(String(250), nullable=True)
    promo_code = Column(String(250), nullable=True)
    potential_monthly_load = Column(BigInteger, nullable=True)
    notes = Column(Text, nullable=True)
    is_whatsapp_tracking_enabled = Column(SmallInteger, nullable=False, server_default='0')
    whatsapp_tracking_charges = Column(Numeric(20,  2), nullable=True, server_default='0.00')

class EntityCallbackUrls(Base):
    __tablename__ = 'entity_callback_urls'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    callback_type = Column(String(255), nullable=False)
    booking_medium = Column(Text, nullable=True)
    callback_url = Column(String(1000), nullable=True)
    transformer = Column(String(10), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)

class EntityChannelMappings(Base):
    __tablename__ = 'entity_channel_mappings'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=False)
    accounts_user_id = Column(Integer, nullable=False)
    accounts_channel_id = Column(Integer, nullable=False)
    channel_id = Column(String(10), nullable=False)
    channel_name = Column(String(50), nullable=False)
    channel_unique_id = Column(String(50), nullable=True)
    channel_url = Column(String(50), nullable=True)
    channel_token = Column(String(255), nullable=True)
    channel_meta = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)
    shop_name = Column(String(255), nullable=True)
    api_version = Column(String(20), nullable=True)

class EntityQuickbookMappings(Base):
    __tablename__ = 'entity_quickbook_mappings'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    gst_branch_id = Column(BigInteger, nullable=True)
    quick_books_id = Column(BigInteger, nullable=True)
    gst_no = Column(String(20), nullable=True)
    email = Column(String(250), nullable=True)
    display_name = Column(String(250), nullable=True)
    entity_name = Column(String(250), nullable=True)
    address = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    parent_quick_books_id = Column(Integer, nullable=True)
    quick_books_data = Column(Text, nullable=True)
    quick_book_balance = Column(Numeric(20,  2), nullable=True)
    invoice_count = Column(Integer, nullable=True, server_default='0')
    payment_count = Column(Integer, nullable=True, server_default='0')

class EntitySalesCommunication(Base):
    __tablename__ = 'entity_sales_communication'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    entity_id = Column(BigInteger, nullable=False)
    reason = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    type = Column(String(100), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class EntitySettings(Base):
    __tablename__ = 'entity_settings'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    email = Column(String(255), nullable=True)
    mobile_number = Column(String(15), nullable=True)
    notify_consignor = Column(SmallInteger, nullable=True, server_default='0')
    report_frequency = Column(SmallInteger, nullable=True, server_default='0')
    label_type = Column(SmallInteger, nullable=True, server_default='0')
    use_cheapest_partner = Column(SmallInteger, nullable=True, server_default='0')
    multi_vendor = Column(SmallInteger, nullable=True, server_default='0')
    display_return_address = Column(SmallInteger, nullable=True, server_default='1')
    thermal_display_value = Column(SmallInteger, nullable=True, server_default='1')
    thermal_display_contact_no = Column(SmallInteger, nullable=True, server_default='1')
    show_consignee_contact = Column(SmallInteger, nullable=True, server_default='1')
    show_gst_number = Column(SmallInteger, nullable=True, server_default='1')
    seller_contact_no = Column(String(50), nullable=True)
    show_escalation_tab = Column(SmallInteger, nullable=False, server_default='0')
    show_discounted_value = Column(SmallInteger, nullable=True, server_default='0')
    manifest_format = Column(SmallInteger, nullable=True, server_default='0')
    is_show_vamaship_logo = Column(SmallInteger, nullable=True, server_default='1')
    brand_name = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    booking_pickup_emailer = Column(SmallInteger, nullable=True, server_default='0')
    fulfill_order = Column(SmallInteger, nullable=True, server_default='1')
    allow_stressed_pincodes_booking = Column(SmallInteger, nullable=True, server_default='1')

class EntityUserMappings(Base):
    __tablename__ = 'entity_user_mappings'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    accounts_user_id = Column(BigInteger, nullable=False)
    is_active = Column(SmallInteger, nullable=False, server_default='1')
    api_key = Column(String(80), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(Time, nullable=True)

class EntityZohobookMappings(Base):
    __tablename__ = 'entity_zohobook_mappings'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    zohobook_id = Column(String(30), nullable=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    gst_branch_id = Column(BigInteger, nullable=True)
    gst_no = Column(String(20), nullable=True)
    email = Column(String(250), nullable=True)
    display_name = Column(String(250), nullable=True)
    entity_name = Column(String(250), nullable=True)
    quick_books_id = Column(BigInteger, nullable=True)
    parent_quick_books_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    address = Column(Text, nullable=True)
    balance = Column(Numeric(20,  2), nullable=True)
    invoice_count = Column(Integer, nullable=True, server_default='0')
    payment_count = Column(Integer, nullable=True, server_default='0')

class EscalationSheet(Base):
    __tablename__ = 'escalation_sheet'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    awb_no = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)
    partner_name = Column(String(255), nullable=True)
    manual_case = Column(String(255), nullable=True)
    partner_remarks = Column(Text, nullable=True)
    followup_remarks = Column(Text, nullable=True)
    vamashipper = Column(String(255), nullable=True)
    source_of_complaint = Column(String(255), nullable=True)
    auto_ticket_status = Column(String(255), nullable=True)
    manual_ticket_status = Column(String(255), nullable=True)
    created_at = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    latest_tracking_status = Column(String(255), nullable=True)
    consignee_name = Column(String(255), nullable=True)
    consignee_no = Column(String(255), nullable=True)
    duplicate_awb = Column(String(255), nullable=True)
    email_subject = Column(String(500), nullable=True)
    last_modified_by = Column(String(255), nullable=True)
    shipment_booking_date = Column(Time, nullable=True)
    seller_name = Column(String(255), nullable=True)
    seller_mobile = Column(String(255), nullable=True)
    entity_id = Column(BigInteger, nullable=True)
    ticket_delay = Column(Integer, nullable=True)
    lr_number = Column(String(255), nullable=True)
    closure_datetime = Column(Time, nullable=True)
    partner_comment_ndr = Column(Text, nullable=True)
    count_of_calls = Column(Integer, nullable=True)
    count_of_ndr = Column(Integer, nullable=True)
    otp_verified_ndr = Column(SmallInteger, nullable=True)
    otp_verified_delivery = Column(SmallInteger, nullable=True)
    edd_partner = Column(String(255), nullable=True)
    reattempt_count = Column(Integer, nullable=True)
    is_closed = Column(SmallInteger, nullable=True, server_default='0')

class FailedJobs(Base):
    __tablename__ = 'failed_jobs'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=True)
    job = Column(Text, nullable=False)
    queue = Column(String(100), nullable=False)
    reason = Column(Text, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    failed_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))

class FraudEntities(Base):
    __tablename__ = 'fraud_entities'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    entity_id = Column(BigInteger, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)

class FraudShipments(Base):
    __tablename__ = 'fraud_shipments'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class FutworkApiLogs(Base):
    __tablename__ = 'futwork_api_logs'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(String(255), nullable=False)
    request = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    status = Column(String(50), nullable=False)
    futwork_unique_id = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    ndr_id = Column(BigInteger, nullable=True)

class InstantCodLogs(Base):
    __tablename__ = 'instant_cod_logs'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=True)
    instant_cod_day = Column(Integer, nullable=True, server_default='0')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class InvoiceCategories(Base):
    __tablename__ = 'invoice_categories'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    category_name = Column(String(20), nullable=True)

class InvoiceData(Base):
    __tablename__ = 'invoice_data'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    invoice_no = Column(String(20), nullable=False)
    excel_data = Column(Text, nullable=False)
    gst_data = Column(Text, nullable=False)
    invoice_data = Column(Text, nullable=False)
    user_gst_details = Column(Text, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)
    ecom2_table_id = Column(BigInteger, nullable=True)

class InvoiceDocTypes(Base):
    __tablename__ = 'invoice_doc_types'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    doc_name = Column(String(20), nullable=True)

class InvoiceLineItems(Base):
    __tablename__ = 'invoice_line_items'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    invoice_no = Column(String(20), nullable=False)
    type_id = Column(Integer, nullable=False)
    doc_type_id = Column(Integer, nullable=False)
    charge_head = Column(String(255), nullable=False)
    remark = Column(String(20), nullable=True)
    sac = Column(Integer, nullable=True)
    qb_line_item_id = Column(Integer, nullable=True)
    tax_code = Column(Integer, nullable=True)
    class_code = Column(String(255), nullable=False)
    amount = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    gst_rate = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    igst_rate = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    cess_rate = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    cgst_amount = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    sgst_amount = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    igst_amount = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    total_gst_amount = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    cess_amount = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    total_amount = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    ecom2_table_id = Column(BigInteger, nullable=True)

class InvoiceTypes(Base):
    __tablename__ = 'invoice_types'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    type_name = Column(String(20), nullable=True)

class InvoicedShipments(Base):
    __tablename__ = 'invoiced_shipments'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    invoice_no = Column(String(20), nullable=True)
    quick_books_id = Column(BigInteger, nullable=True)
    invoiced_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    invoice_date = Column(DateTime, nullable=True)
    invoice_data = Column(Text, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)
    ecom2_table_id = Column(BigInteger, nullable=True)

class Invoices(Base):
    __tablename__ = 'invoices'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=True)
    accounts_user_id = Column(Integer, nullable=True)
    invoice_no = Column(String(20), nullable=True)
    against_invoice_no = Column(String(255), nullable=True)
    category_id = Column(Integer, nullable=False, server_default='1')
    invoice_type = Column(String(20), nullable=False)
    invoice_ref_no = Column(String(30), nullable=True)
    data = Column(Text, nullable=False)
    total_without_tax = Column(Numeric(20,  2), nullable=False)
    tax = Column(Numeric(5,  2), nullable=True)
    service_tax = Column(Numeric(20,  2), nullable=True)
    swachh_bharat_cess = Column(Numeric(20,  2), nullable=True)
    krishi_kalyan_cess = Column(Numeric(20,  2), nullable=True)
    igst = Column(Numeric(20,  2), nullable=True)
    sgst = Column(Numeric(20,  2), nullable=True)
    cgst = Column(Numeric(20,  2), nullable=True)
    tax_total = Column(Numeric(20,  2), nullable=True)
    duty_amount = Column(Numeric(20,  2), nullable=True)
    total = Column(Numeric(20,  2), nullable=False)
    paid = Column(Numeric(20,  2), nullable=True)
    pending = Column(Numeric(20,  2), nullable=True)
    quick_books_id = Column(String(20), nullable=True)
    qb_transaction_id = Column(String(50), nullable=True)
    qb_amount = Column(Numeric(20,  2), nullable=True)
    payment_data = Column(Text, nullable=True)
    status = Column(SmallInteger, nullable=True, server_default='0')
    email_status = Column(Integer, nullable=True, server_default='0')
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    valuable = Column(SmallInteger, nullable=True, server_default='0')
    remark = Column(String(50), nullable=True)
    file_link = Column(Text, nullable=True)
    invoice_date = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    gst_branch_id = Column(Integer, nullable=True)
    e_invoice_exists = Column(SmallInteger, nullable=True, server_default='0')
    e_invoice_details = Column(Text, nullable=True)
    payment_received = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    is_paid = Column(SmallInteger, nullable=False, server_default='0')

class LocationWarehouseMappings(Base):
    __tablename__ = 'location_warehouse_mappings'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    partner_id = Column(Integer, nullable=False)
    location_id = Column(BigInteger, nullable=False)
    warehouse_id = Column(String(255), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)
    hash = Column(String(255), nullable=True)

class Locations(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    accounts_user_id = Column(BigInteger, nullable=True)
    gst_branch_id = Column(Integer, nullable=True)
    location_name = Column(String(100), nullable=True)
    location_type = Column(String(50), nullable=True)
    email = Column(String(200), nullable=True)
    full_name = Column(String(200), nullable=False)
    contact = Column(String(25), nullable=True)
    calling_code = Column(String(10), nullable=True)
    address_line_1 = Column(String(255), nullable=True)
    address_line_2 = Column(String(100), nullable=True)
    address_line_3 = Column(String(100), nullable=True)
    landmark = Column(String(50), nullable=True)
    pincode = Column(String(50), nullable=True)
    city = Column(String(50), nullable=True)
    state = Column(String(50), nullable=True)
    visibility = Column(SmallInteger, nullable=False, server_default='0')
    country = Column(String(50), nullable=True)
    open_time = Column(DateTime, nullable=True)
    closed_time = Column(DateTime, nullable=True)
    lat = Column(Numeric(20,  10), nullable=True)
    long = Column(Numeric(20,  10), nullable=True)
    channel_name = Column(String(50), nullable=True)
    channel_location_id = Column(String(100), nullable=True)
    channel_unique_id = Column(String(50), nullable=True)
    is_active = Column(SmallInteger, nullable=False, server_default='1')
    vendor_pan_no = Column(String(100), nullable=True)
    vendor_gst_no = Column(String(100), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)
    hash_sha256 = Column(String(64), nullable=True)

class LogAirDomPincodes(Base):
    __tablename__ = 'log_air_dom_pincodes'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=True, server_default='0')
    durations = Column(Text, nullable=True)
    has_cod = Column(SmallInteger, nullable=True, server_default='0')
    has_express = Column(SmallInteger, nullable=True, server_default='0')
    has_cash = Column(SmallInteger, nullable=True, server_default='0')
    has_repl = Column(SmallInteger, nullable=True, server_default='0')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    cron_batch_id = Column(String(255), nullable=True)

class LogSurfaceB2bPincodes(Base):
    __tablename__ = 'log_surface_b2b_pincodes'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=True, server_default='0')
    has_cod = Column(SmallInteger, nullable=True, server_default='0')
    has_express = Column(SmallInteger, nullable=True, server_default='0')
    has_cash = Column(SmallInteger, nullable=True, server_default='0')
    has_repl = Column(SmallInteger, nullable=True, server_default='0')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    cron_batch_id = Column(String(255), nullable=True)

class LogSurfaceB2cPincodes(Base):
    __tablename__ = 'log_surface_b2c_pincodes'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=True, server_default='0')
    durations = Column(Text, nullable=True)
    has_cod = Column(SmallInteger, nullable=True, server_default='0')
    has_express = Column(SmallInteger, nullable=True, server_default='0')
    has_cash = Column(SmallInteger, nullable=True, server_default='0')
    has_repl = Column(SmallInteger, nullable=True, server_default='0')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    cron_batch_id = Column(String(255), nullable=True)

class ManualTrackableShipments(Base):
    __tablename__ = 'manual_trackable_shipments'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    tracking_id = Column(String(20), nullable=False)
    supplier_id = Column(Integer, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class Ndr(Base):
    __tablename__ = 'ndr'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    awb_no = Column(String(255), nullable=False)
    customer_reference_number_1 = Column(String(150), nullable=True)
    customer_reference_number_2 = Column(String(150), nullable=True)
    supplier_id = Column(Integer, nullable=True)
    tracking_status_code = Column(Integer, nullable=True)
    partner_comment = Column(String(255), nullable=True)
    consignee_name = Column(String(255), nullable=False)
    consignee_number = Column(String(150), nullable=False)
    accounts_entity_id = Column(Integer, nullable=False)
    accounts_user_id = Column(Integer, nullable=False)
    customer_response = Column(SmallInteger, nullable=True)
    customer_comment = Column(String(255), nullable=True)
    consignee_response = Column(SmallInteger, nullable=True)
    consignee_comment = Column(String(255), nullable=True)
    updated_by = Column(String(50), nullable=True)
    ndr_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    dispatch_count = Column(SmallInteger, nullable=True, server_default='0')
    undelivered_count = Column(SmallInteger, nullable=True, server_default='0')
    ndr_replied_at = Column(Time, nullable=True)

class NdrApiLogs(Base):
    __tablename__ = 'ndr_api_logs'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tracking_id = Column(String(100), nullable=False)
    shipment_no = Column(BigInteger, nullable=False)
    ndr_id = Column(BigInteger, nullable=True)
    accounts_entity_Id = Column(BigInteger, nullable=False)
    request = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    ndr_response = Column(String(15), nullable=True)
    created_at = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True)

class NdrReport(Base):
    __tablename__ = 'ndr_report'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_number = Column(Integer, nullable=False)
    customer_reference_number = Column(String(255), nullable=False)
    pickup_date = Column(DateTime, nullable=True)
    consignee_name = Column(String(255), nullable=False)
    consignee_number = Column(String(255), nullable=False)
    consignee_email_id = Column(String(255), nullable=False)
    destination_city = Column(String(255), nullable=False)
    tracking_status = Column(String(255), nullable=False)
    delivery_attempts = Column(Integer, nullable=False)
    partner_reason = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    order_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    awb_no = Column(String(255), nullable=False)
    ndr_date = Column(DateTime, nullable=True)
    comment = Column(Text, nullable=False)
    extra_comment = Column(String(255), nullable=False)
    extra = Column(Text, nullable=False)
    partner = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)
    dispatched_attempts = Column(Integer, nullable=False, server_default='0')
    undelivered_attempts = Column(Integer, nullable=False, server_default='0')
    consignee_response = Column(String(255), nullable=True)
    consignee_comment = Column(String(255), nullable=True)

class NotificationLogs(Base):
    __tablename__ = 'notification_logs'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    event = Column(String(200), nullable=True)
    notification_type = Column(String(30), nullable=True)
    notification_content = Column(String(500), nullable=True)
    recipient_contact = Column(String(200), nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

class Npr(Base):
    __tablename__ = 'npr'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    vamaship_location_id = Column(BigInteger, nullable=False)
    accounts_entity_id = Column(BigInteger, nullable=False)
    partner_id = Column(BigInteger, nullable=False)
    partner_warehouse_id = Column(String(255), nullable=True)
    partner_comment = Column(String(800), nullable=True)
    npr_date = Column(Date, nullable=True)
    shipment_no = Column(BigInteger, nullable=True)
    shipment_count = Column(Integer, nullable=True)
    customer_response = Column(SmallInteger, nullable=True)
    customer_comment = Column(String(500), nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

class NumberSeriess(Base):
    __tablename__ = 'number_seriess'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    type = Column(String(20), nullable=False)
    prefix = Column(String(20), nullable=False)
    next_char = Column(String(3), nullable=False)
    next = Column(Integer, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class OcrResults(Base):
    __tablename__ = 'ocr_results'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(String(255), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    link = Column(String(500), nullable=False)
    ocr_engine = Column(String(50), nullable=False)
    category = Column(String(255), nullable=True)
    ocr_text = Column(Text, nullable=True)
    extracted_data = Column(Text, nullable=True)
    raw_results = Column(Text, nullable=True)

class OfflineOrders(Base):
    __tablename__ = 'offline_orders'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    tracking_id = Column(String(20), nullable=False)
    accounts_entity_id = Column(Integer, nullable=False)
    supplier_id = Column(Integer, nullable=False)
    product_code = Column(String(10), nullable=False)
    shipment_date = Column(Time, nullable=True)
    pickup_address = Column(String(200), nullable=True)
    pickup_pincode = Column(String(10), nullable=True)
    consignee_name = Column(String(200), nullable=True)
    consignee_email = Column(String(100), nullable=True)
    consignee_mobile = Column(String(20), nullable=True)
    consignee_address = Column(String(200), nullable=True)
    consignee_pincode = Column(String(20), nullable=True)
    product = Column(String(200), nullable=True)
    product_value = Column(Numeric(20,  2), nullable=True)
    product_weight = Column(Numeric(20,  2), nullable=True)
    cod_value = Column(Numeric(20,  2), nullable=True)
    quantity = Column(Integer, nullable=True, server_default='1')
    reference = Column(String(20), nullable=True)
    created_at = Column(Time, nullable=True)
    updated_at = Column(Time, nullable=True)
    deleted_at = Column(Time, nullable=True)
    uploaded_by = Column(Integer, nullable=True)
    addtional_data = Column(Text, nullable=True)
    status = Column(SmallInteger, nullable=True)
    errors = Column(Text, nullable=True)

class OnlinePaymentRequests(Base):
    __tablename__ = 'online_payment_requests'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    mobile = Column(String(15), nullable=False)
    amount = Column(Float, nullable=False)
    product = Column(String(50), nullable=False)
    payment_token = Column(String(255), nullable=False)
    accounts_user_id = Column(Integer, nullable=False)
    accounts_entity_id = Column(Integer, nullable=False)
    ecom2_user_id = Column(Integer, nullable=True)
    ecom2_master_user_id = Column(Integer, nullable=True)
    bulk_id = Column(String(30), nullable=True)
    gateway_request_id = Column(String(150), nullable=True)
    transaction_unique_id = Column(String(150), nullable=True)
    payment_status = Column(String(50), nullable=True)
    payment_mode = Column(String(50), nullable=True)
    received_amount = Column(Float, nullable=True)
    error_message = Column(String(150), nullable=True)
    request_parameters = Column(Text, nullable=True)
    payment_response = Column(Text, nullable=True)
    gateway_name = Column(String(30), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)

class OrderRisks(Base):
    __tablename__ = 'order_risks'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    order_id = Column(BigInteger, nullable=True)
    message = Column(String(255), nullable=True)
    score = Column(Float, nullable=False)
    cause_cancel = Column(SmallInteger, nullable=True, server_default='0')
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False)

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=False)
    accounts_user_id = Column(Integer, nullable=False)
    quote_request_id = Column(BigInteger, nullable=True)
    shipment_no = Column(BigInteger, nullable=True)
    channel_mapping_id = Column(Integer, nullable=True)
    channel_order_id = Column(String(50), nullable=True)
    channel_id = Column(String(10), nullable=False)
    channel_name = Column(String(50), nullable=False)
    bulk_id = Column(String(20), nullable=True)
    payment_type = Column(String(50), nullable=False)
    from_pincode = Column(String(10), nullable=True)
    to_pincode = Column(String(10), nullable=True)
    order_date = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    shipment_date = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    cod_value = Column(Numeric(10,  2), nullable=False, server_default='0.00')
    product_value = Column(Numeric(10,  2), nullable=False, server_default='0.00')
    currency_code = Column(String(10), nullable=False)
    product = Column(String(255), nullable=True)
    weight = Column(Numeric(20,  2), nullable=False, server_default='0.50')
    weight_unit = Column(String(10), nullable=False)
    weight_in_kgs = Column(Numeric(20,  2), nullable=False)
    quantity = Column(Integer, nullable=False, server_default='1')
    is_offline = Column(SmallInteger, nullable=False, server_default='0')
    cancelled_at = Column(DateTime, nullable=True)
    reference1 = Column(String(50), nullable=True)
    reference2 = Column(String(50), nullable=True)
    status = Column(String(50), nullable=False)
    whatsapp_status = Column(String(50), nullable=True)
    gst_branch_id = Column(Integer, nullable=True)
    pickup_location_id = Column(Integer, nullable=True)
    consignee_location_id = Column(Integer, nullable=False)
    billing_location_id = Column(Integer, nullable=True)
    return_location_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)
    ip_address = Column(String(25), nullable=True)
    booking_medium = Column(String(25), nullable=True)
    tags = Column(String(255), nullable=True)

class PackageMasters(Base):
    __tablename__ = 'package_masters'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=False)
    accounts_user_id = Column(Integer, nullable=True)
    package_identifier = Column(String(50), nullable=False)
    channel_mapping_id = Column(Integer, nullable=True)
    channel_name = Column(String(200), nullable=False)
    autogenerated = Column(SmallInteger, nullable=True, server_default='0')
    length = Column(Numeric(5,  2), nullable=False, server_default='1.00')
    breadth = Column(Numeric(5,  2), nullable=False, server_default='1.00')
    height = Column(Numeric(5,  2), nullable=False, server_default='1.00')
    unit = Column(String(10), nullable=False)
    default_package = Column(SmallInteger, nullable=True, server_default='0')
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)

class PartnerAirCosting(Base):
    __tablename__ = 'partner_air_costing'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    costing_logic = Column(String(255), nullable=False)
    per_slab_cost = Column(Text, nullable=False)
    service_tax = Column(Float, nullable=True, server_default='0.0000')
    fuel_surcharge = Column(Float, nullable=False)
    cod_tax = Column(String(100), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    from_date = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    classes = Column(Text, nullable=True)
    extra_charges = Column(Text, nullable=False)
    volumetric_formula = Column(String(255), nullable=False)
    is_reverse = Column(SmallInteger, nullable=False, server_default='0')
    is_rto = Column(SmallInteger, nullable=True, server_default='0')

class PartnerAirPincodes(Base):
    __tablename__ = 'partner_air_pincodes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=False, server_default='0')
    durations = Column(Text, nullable=True)
    has_cod = Column(SmallInteger, nullable=False)
    has_express = Column(SmallInteger, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    has_cash = Column(SmallInteger, nullable=False)
    has_repl = Column(SmallInteger, nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    region = Column(String(100), nullable=False)
    from_date = Column(DateTime, nullable=True)

class PartnerBookingJobs(Base):
    __tablename__ = 'partner_booking_jobs'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    supplier_id = Column(BigInteger, nullable=False)
    reference = Column(String(100), nullable=False)
    status = Column(String(20), nullable=True)

class PartnerConnectSupplierSettings(Base):
    __tablename__ = 'partner_connect_supplier_settings'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(BigInteger, nullable=False)
    name = Column(String(255), nullable=False)
    class_name = Column(String(100), nullable=False)
    settings = Column(Text, nullable=False)
    endpoints = Column(Text, nullable=False)

class PartnerGroups(Base):
    __tablename__ = 'partner_groups'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    partner_alias = Column(String(50), nullable=False)
    master_partner_id = Column(Integer, nullable=False)
    common_coverage = Column(SmallInteger, nullable=False)
    common_tracking_codes = Column(SmallInteger, nullable=False)
    common_partner_connect_settings = Column(SmallInteger, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

class PartnerPincodeMaster(Base):
    __tablename__ = 'partner_pincode_master'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(String(8), nullable=False)
    city = Column(String(200), nullable=False)
    state = Column(String(200), nullable=False)
    region = Column(String(50), nullable=True)
    type = Column(String(20), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class PartnerPincodes(Base):
    __tablename__ = 'partner_pincodes'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(BigInteger, nullable=False)
    pincode = Column(String(10), nullable=False)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    region = Column(String(100), nullable=True)
    from_date = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    to_date = Column(Time, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(Time, nullable=True)
    additional_config = Column(Text, nullable=True)

class PartnerRuleSets(Base):
    __tablename__ = 'partner_rule_sets'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=False)
    rank = Column(Integer, nullable=False)
    rule_set_name = Column(String(100), nullable=False)
    service_type = Column(String(255), nullable=False)
    product_code = Column(String(6), nullable=False)
    suppliers = Column(String(300), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    active = Column(SmallInteger, nullable=False, server_default='1')
    deleted_at = Column(DateTime, nullable=True)

class PartnerRules(Base):
    __tablename__ = 'partner_rules'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    rule_set_id = Column(Integer, nullable=False)
    rule_type = Column(String(255), nullable=False)
    rank = Column(Integer, nullable=False)
    config = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    active = Column(SmallInteger, nullable=False, server_default='1')
    deleted_at = Column(DateTime, nullable=True)

class PartnerSharedMappings(Base):
    __tablename__ = 'partner_shared_mappings'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    partner_id = Column(BigInteger, nullable=False)
    tracking_partner = Column(BigInteger, nullable=True)
    coverage_partner = Column(BigInteger, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)
    awb_no_partner = Column(BigInteger, nullable=True)

class PartnerSurfaceB2bPincodes(Base):
    __tablename__ = 'partner_surface_b2b_pincodes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=False, server_default='0')
    has_cod = Column(SmallInteger, nullable=False, server_default='0')
    has_express = Column(SmallInteger, nullable=False, server_default='0')
    has_cash = Column(SmallInteger, nullable=False, server_default='0')
    has_repl = Column(SmallInteger, nullable=False, server_default='0')
    is_oda = Column(SmallInteger, nullable=True, server_default='0')
    zone = Column(String(10), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    disabled_on = Column(Time, nullable=True)
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    region = Column(String(100), nullable=False)

class PartnerSurfaceB2cPincodes(Base):
    __tablename__ = 'partner_surface_b2c_pincodes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=False, server_default='0')
    durations = Column(Text, nullable=True)
    has_cod = Column(SmallInteger, nullable=False)
    has_express = Column(SmallInteger, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    has_cash = Column(SmallInteger, nullable=False)
    has_repl = Column(SmallInteger, nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    region = Column(String(100), nullable=False)
    from_date = Column(DateTime, nullable=True)

class PartnerSurfaceCosting(Base):
    __tablename__ = 'partner_surface_costing'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    costing_logic = Column(String(255), nullable=False)
    per_slab_cost = Column(Text, nullable=False)
    fuel_surcharge = Column(Float, nullable=False)
    cod_tax = Column(String(100), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    from_date = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    classes = Column(Text, nullable=True)
    extra_charges = Column(Text, nullable=False)
    volumetric_formula = Column(String(255), nullable=False)
    is_reverse = Column(SmallInteger, nullable=False, server_default='0')
    is_rto = Column(SmallInteger, nullable=True, server_default='0')

class PartnerTrackingCodes(Base):
    __tablename__ = 'partner_tracking_codes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    partner_tracking_code = Column(String(255), nullable=True)
    vamaship_tracking_code = Column(String(255), nullable=True)
    partner_id = Column(Integer, nullable=False, server_default='0')
    deactivated_on = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=True, server_default=text('current_timestamp()'))

class Passbook(Base):
    __tablename__ = 'passbook'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    remark = Column(Text, nullable=True)
    credit_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    debit_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    running_balance = Column(Numeric(18,  2), nullable=False, server_default='0.00')
    ledger_amount = Column(Numeric(18,  2), nullable=False)
    ledger_event_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    vama_transaction_id = Column(BigInteger, nullable=False)
    accounts_entity_id = Column(Integer, nullable=True)
    payment_mode = Column(String(100), nullable=True)
    payment_type = Column(String(20), nullable=True)
    sac = Column(BigInteger, nullable=True)
    voucher_no = Column(String(30), nullable=True)
    accounts_user_id = Column(Integer, nullable=True)
    accounting_type_id = Column(Integer, nullable=False)
    transaction_amount = Column(Numeric(20,  2), nullable=False)
    transaction_unique_id = Column(String(100), nullable=True)
    transaction_by = Column(BigInteger, nullable=False)
    invoice_no = Column(String(50), nullable=True)
    quick_books_id = Column(String(20), nullable=True)
    qb_transaction_id = Column(String(50), nullable=True)
    qb_payment_id = Column(String(50), nullable=True)
    status = Column(SmallInteger, nullable=False, server_default='0')
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)
    gateway_name = Column(String(255), nullable=True)
    payment_request_token = Column(String(255), nullable=True)
    payment_status = Column(String(255), nullable=True)
    reference_table = Column(String(255), nullable=True)
    reference_id = Column(String(255), nullable=True)
    received_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    transaction_status = Column(SmallInteger, nullable=True, server_default='0')
    zohobook_id = Column(String(30), nullable=True)
    source_tx_id = Column(BigInteger, nullable=False)
    operation = Column(String(255), nullable=True)

class PaymentGatewayMaster(Base):
    __tablename__ = 'payment_gateway_master'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    payment_gateway_name = Column(String(150), nullable=False)
    payment_response_transaction_id_field_name = Column(String(150), nullable=False)
    fields_mapping_array = Column(Text, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    updated_at = Column(Time, nullable=False)
    deleted_at = Column(Time, nullable=True)

class PaymentHistories(Base):
    __tablename__ = 'payment_histories'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    received_amount = Column(Numeric(10,  2), nullable=False, server_default='0.00')
    gateway_master_id = Column(Integer, nullable=True)
    gateway_request_id = Column(String(255), nullable=True)
    transaction_unique_id = Column(String(255), nullable=False)
    used_amount = Column(Numeric(10,  2), nullable=False, server_default='0.00')
    unused_amount = Column(Numeric(10,  2), nullable=False, server_default='0.00')
    created_at = Column(Time, nullable=False)
    updated_at = Column(Time, nullable=False)
    deleted_at = Column(Time, nullable=True)

class PayuCallbackLogs(Base):
    __tablename__ = 'payu_callback_logs'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    request_host = Column(String(100), nullable=True)
    request_json = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

class PeriscopeDashboards(Base):
    __tablename__ = 'periscope_dashboards'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dashboard_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    enable_filters = Column(Text, nullable=True)
    created_at = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class PickupApiLogs(Base):
    __tablename__ = 'pickup_api_logs'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    location_id = Column(BigInteger, nullable=False)
    supplier_id = Column(BigInteger, nullable=False)
    pickup_id = Column(String(30), nullable=True)
    request = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=True, server_default=text('current_timestamp()'))

class PickupApiLogs2(Base):
    __tablename__ = 'pickup_api_logs2'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    location_id = Column(BigInteger, nullable=False)
    supplier_id = Column(BigInteger, nullable=False)
    pickup_id = Column(String(30), nullable=True)
    request = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=True, server_default=text('current_timestamp()'))

class PickupIds(Base):
    __tablename__ = 'pickup_ids'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    accounts_user_id = Column(BigInteger, nullable=False)
    pickup_address = Column(String(1000), nullable=False)
    location_id = Column(BigInteger, nullable=True)
    supplier_id = Column(Integer, nullable=False)
    pickup_id = Column(String(255), nullable=False)
    weight_sent = Column(Float, nullable=False)
    package_count_sent = Column(Integer, nullable=False)
    pickup_id_date = Column(DateTime, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class PincodeAreaCodeMaps(Base):
    __tablename__ = 'pincode_area_code_maps'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    pincode = Column(BigInteger, nullable=False)
    area_code = Column(String(10), nullable=False)
    sc_code = Column(String(10), nullable=False)

class PricingPlans(Base):
    __tablename__ = 'pricing_plans'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(50), nullable=True)
    description = Column(String(255), nullable=True)
    linked_entity_id = Column(BigInteger, nullable=True)
    from_date = Column(DateTime, nullable=False)
    to_date = Column(DateTime, nullable=True)
    creator = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False)

class ProductMasters(Base):
    __tablename__ = 'product_masters'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    product_code = Column(String(255), nullable=False)
    product_name = Column(String(255), nullable=False)
    service_type = Column(String(255), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=False)
    channel_mapping_id = Column(Integer, nullable=True)
    channel_product_id = Column(BigInteger, nullable=True)
    channel_variant_id = Column(BigInteger, nullable=True)
    channel_id = Column(String(10), nullable=False)
    channel_name = Column(String(50), nullable=False)
    product_name = Column(String(255), nullable=False)
    brand = Column(String(150), nullable=True)
    product_type = Column(String(255), nullable=True)
    price = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    currency = Column(String(5), nullable=True)
    sku = Column(String(50), nullable=True)
    hsn_code = Column(Integer, nullable=True, server_default='0')
    weight = Column(Numeric(8,  2), nullable=True, server_default='0.50')
    weight_unit = Column(String(10), nullable=True)
    weight_in_kgs = Column(Numeric(5,  2), nullable=True, server_default='0.50')
    inventory_quantity = Column(Integer, nullable=True, server_default='0')
    length = Column(Numeric(5,  2), nullable=True, server_default='1.00')
    breadth = Column(Numeric(5,  2), nullable=True, server_default='1.00')
    height = Column(Numeric(5,  2), nullable=True, server_default='1.00')
    unit = Column(String(10), nullable=True)
    product_meta = Column(Text, nullable=True)
    product_images = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)

class PromoCodeRedemptions(Base):
    __tablename__ = 'promo_code_redemptions'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=False)
    accounts_user_id = Column(Integer, nullable=True)
    promo_code = Column(String(20), nullable=False)
    promo_code_id = Column(Integer, nullable=False)
    transaction_id = Column(BigInteger, nullable=True)
    created_at = Column(Time, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class PromoCodes(Base):
    __tablename__ = 'promo_codes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    promo_code = Column(String(50), nullable=False)
    promo_name = Column(String(100), nullable=False)
    promo_description = Column(Text, nullable=True)
    promo_type = Column(String(50), nullable=False)
    promo_category = Column(String(30), nullable=False)
    accounts_entity_id = Column(Integer, nullable=True)
    promo_amount = Column(Numeric(12,  2), nullable=False, server_default='0.00')
    status = Column(SmallInteger, nullable=False, server_default='1')
    promo_started_at = Column(Time, nullable=True)
    promo_ennded_at = Column(Time, nullable=True)
    created_at = Column(Time, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    deleted_at = Column(Time, nullable=True)

class QuickBookHooks(Base):
    __tablename__ = 'quick_book_hooks'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    value = Column(Text, nullable=False)
    status = Column(SmallInteger, nullable=False, server_default='0')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class QuickbookInvoices(Base):
    __tablename__ = 'quickbook_invoices'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    invoice_no = Column(String(20), nullable=False)
    type = Column(String(20), nullable=True)
    ref_invoice_no = Column(String(20), nullable=True)
    quick_books_id = Column(Integer, nullable=False)
    user_quick_books_id = Column(Integer, nullable=False)
    invoice_amount = Column(Numeric(20,  2), nullable=False)
    quick_book_balance = Column(Numeric(20,  2), nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class QuickbooksSetting(Base):
    __tablename__ = 'quickbooks_setting'

    qb_id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    ref_code = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)
    status = Column(SmallInteger, nullable=False)
    is_default = Column(SmallInteger, nullable=False)
    created_by = Column(BigInteger, nullable=False)
    updated_by = Column(BigInteger, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class QuoteRequests(Base):
    __tablename__ = 'quote_requests'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=False)
    reference_no = Column(String(20), nullable=False)
    is_from_channel = Column(SmallInteger, nullable=True, server_default='0')
    request_data = Column(Text, nullable=False)
    supporting_data = Column(Text, nullable=False)
    response_data = Column(Text, nullable=True)
    quote_total = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    quote_status = Column(SmallInteger, nullable=False, server_default='0')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)

class Reconciliations(Base):
    __tablename__ = 'reconciliations'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=False)
    quickbooks_id = Column(Integer, nullable=False)
    erp_invoice_count = Column(Integer, nullable=False)
    erp_invoice_amount = Column(Numeric(20,  2), nullable=False)
    qb_invoice_count = Column(Integer, nullable=False)
    qb_invoice_amount = Column(Numeric(20,  2), nullable=False)
    invoice_diff = Column(Numeric(20,  2), nullable=False)
    erp_payment_count = Column(Integer, nullable=False)
    erp_payment_amount = Column(Numeric(20,  2), nullable=False)
    qb_payment_count = Column(Integer, nullable=False)
    qb_payment_amount = Column(Numeric(20,  2), nullable=False)
    payment_diff = Column(Numeric(20,  2), nullable=False)
    erp_creditnote_count = Column(Integer, nullable=False)
    erp_creditnote_amount = Column(Numeric(20,  2), nullable=False)
    qb_creditnote_count = Column(Integer, nullable=False)
    qb_creditnote_amount = Column(Numeric(20,  2), nullable=False)
    creditnote_diff = Column(Numeric(20,  2), nullable=False)
    erp_jv_count = Column(Integer, nullable=False)
    erp_jv_amount = Column(Numeric(20,  2), nullable=False)
    qb_jv_count = Column(Integer, nullable=False)
    qb_jv_amount = Column(Numeric(20,  2), nullable=False)
    jv_diff = Column(Numeric(20,  2), nullable=False)
    erp_wallet_amount = Column(Numeric(20,  2), nullable=False)
    qb_outstanding = Column(Numeric(20,  2), nullable=False)
    un_invoiced_amount = Column(Numeric(20,  2), nullable=False)
    wallet_diff = Column(Numeric(20,  2), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class Refunds(Base):
    __tablename__ = 'refunds'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    request_token = Column(String(255), nullable=False)
    shipment_amount = Column(Numeric(20,  2), nullable=False)
    credit_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    refund_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    transaction_id = Column(String(10), nullable=True)
    refund_mode = Column(String(10), nullable=True)
    refund_to = Column(String(10), nullable=True)
    reason_type = Column(Integer, nullable=True)
    reason = Column(String(255), nullable=True)
    remark = Column(Text, nullable=True)
    request_by = Column(BigInteger, nullable=True)
    status = Column(SmallInteger, nullable=True, server_default='0')
    refund_transction_id = Column(String(255), nullable=True)
    quick_book_id = Column(String(30), nullable=True)
    respond_by = Column(BigInteger, nullable=True)
    respond_remark = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    deleted_at = Column(Time, nullable=True)

class SalesPersonTarget(Base):
    __tablename__ = 'sales_person_target'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    employee_id = Column(BigInteger, nullable=False)
    target_type = Column(String(100), nullable=False)
    target_value = Column(BigInteger, nullable=False)
    target_month = Column(String(20), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class SeriesBulkId(Base):
    __tablename__ = 'series_bulk_id'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    stub = Column(String(1), nullable=True)

class SeriesCod(Base):
    __tablename__ = 'series_cod'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    stub = Column(String(1), nullable=True)

class SeriesRefund(Base):
    __tablename__ = 'series_refund'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    stub = Column(String(1), nullable=True)

class SeriesShipment(Base):
    __tablename__ = 'series_shipment'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    stub = Column(String(1), nullable=True)

class SeriesTransaction(Base):
    __tablename__ = 'series_transaction'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    stub = Column(String(1), nullable=True)

class ShipmentAdditionalCharges(Base):
    __tablename__ = 'shipment_additional_charges'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    type = Column(String(20), nullable=True)
    charge_head = Column(String(100), nullable=True)
    amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    remark = Column(String(255), nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(Time, nullable=True)
    updated_at = Column(Time, nullable=True)

class ShipmentAddresses(Base):
    __tablename__ = 'shipment_addresses'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    type = Column(SmallInteger, nullable=True)
    shipment_no = Column(BigInteger, nullable=False)
    full_name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    contact = Column(String(255), nullable=True)
    calling_code = Column(String(5), nullable=True)
    address_line_1 = Column(String(255), nullable=True)
    address_line_2 = Column(String(100), nullable=True)
    address_line_3 = Column(String(100), nullable=True)
    landmark = Column(String(100), nullable=True)
    pincode = Column(String(50), nullable=True)
    city = Column(String(50), nullable=True)
    state = Column(String(50), nullable=True)
    country = Column(String(50), nullable=True)
    location_type = Column(String(50), nullable=True)
    location_name = Column(String(100), nullable=True)
    location_id = Column(BigInteger, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class ShipmentAwbHistories(Base):
    __tablename__ = 'shipment_awb_histories'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    awb_number = Column(String(255), nullable=False)
    awb_category = Column(String(255), nullable=False)
    awb_category_id = Column(Integer, nullable=False)
    awb_cost = Column(Numeric(8,  2), nullable=False)
    awb_weight = Column(Numeric(8,  2), nullable=False)
    partner_name = Column(String(255), nullable=False)
    partner_id = Column(Integer, nullable=True)
    added_by = Column(Integer, nullable=True)
    remark = Column(String(255), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class ShipmentBookingWeights(Base):
    __tablename__ = 'shipment_booking_weights'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    actual_weight = Column(Numeric(20,  2), nullable=False)
    weight_decrease = Column(Numeric(20,  2), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class ShipmentBuyPrice(Base):
    __tablename__ = 'shipment_buy_price'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(String(50), nullable=False)
    total_without_tax = Column(Numeric(12,  2), nullable=True)
    total_with_tax = Column(Numeric(12,  2), nullable=True)
    total_tax = Column(Numeric(12,  2), nullable=True)
    volumetric_weight = Column(Numeric(10,  2), nullable=True)
    dead_weight = Column(Numeric(10,  2), nullable=True)
    applied_weight = Column(Numeric(10,  2), nullable=True)
    zone = Column(String(10), nullable=False)
    slab_count = Column(Integer, nullable=True)
    freight = Column(Numeric(10,  2), nullable=True)
    fuel_surcharge = Column(Numeric(10,  2), nullable=True)
    cod_charge = Column(Numeric(10,  2), nullable=True)
    rto_charge = Column(Numeric(10,  2), nullable=True)
    oda_charge = Column(Numeric(10,  2), nullable=True)
    opa_charge = Column(Numeric(10,  2), nullable=True)
    docket_charge = Column(Numeric(10,  2), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class ShipmentCancellationRequests(Base):
    __tablename__ = 'shipment_cancellation_requests'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    accounts_entity_id = Column(BigInteger, nullable=False)
    accounts_user_id = Column(Integer, nullable=False)
    tracking_id = Column(String(255), nullable=True)
    cancellation_status = Column(SmallInteger, nullable=False)
    user_reason = Column(String(300), nullable=True)
    cc_reason = Column(String(300), nullable=True)
    user_remark = Column(String(300), nullable=True)
    cc_remark = Column(String(300), nullable=True)
    cancel_requested_by = Column(BigInteger, nullable=True)
    refund_amount = Column(Float, nullable=False)
    approved_by = Column(BigInteger, nullable=False, server_default='0')
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    refund_to = Column(String(300), nullable=False)
    deleted_at = Column(Time, nullable=True)

class ShipmentCostBreakups(Base):
    __tablename__ = 'shipment_cost_breakups'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ecom2_table_id = Column(Integer, nullable=True)
    shipment_no = Column(BigInteger, nullable=False)
    charge_head = Column(String(255), nullable=False)
    sac = Column(Integer, nullable=True)
    class_code = Column(String(255), nullable=True)
    amount = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    gst = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    cgst = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    sgst = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    igst = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    total_gst = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    total_amount = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)

class ShipmentEscalations(Base):
    __tablename__ = 'shipment_escalations'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=True)
    shipment_no = Column(BigInteger, nullable=True)
    order_no = Column(String(50), nullable=True)
    awb_no = Column(String(255), nullable=True)
    agent = Column(String(100), nullable=True)
    supplier_id = Column(Integer, nullable=True)
    supplier_name = Column(String(100), nullable=True)
    shipper_remarks = Column(String(200), nullable=True)
    vamaship_remark = Column(String(200), nullable=True)
    subject_request = Column(String(200), nullable=True)
    manual_case = Column(String(250), nullable=True)
    case_status = Column(String(200), nullable=True)
    last_updated_by = Column(String(50), nullable=True)
    vamashipper = Column(String(200), nullable=True)
    follow_up = Column(String(200), nullable=True)
    hidden_at = Column(String(200), nullable=True)
    closed_at = Column(Time, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class ShipmentInputs(Base):
    __tablename__ = 'shipment_inputs'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    accounts_entity_id = Column(Integer, nullable=False)
    accounts_user_id = Column(Integer, nullable=False)
    order_id = Column(Integer, nullable=True)
    gst_number = Column(String(20), nullable=True)
    shipment_type = Column(String(50), nullable=True)
    mode_transport = Column(String(20), nullable=True)
    cargo_type = Column(String(100), nullable=False)
    service_type = Column(String(20), nullable=True)
    shipment_date = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    requested_pickup_date = Column(DateTime, nullable=True, server_default=text('current_timestamp()'))
    package_count = Column(Integer, nullable=False)
    product_value = Column(Numeric(20,  2), nullable=False)
    weight_in_kgs = Column(Numeric(20,  2), nullable=True)
    reference1 = Column(String(50), nullable=True)
    reference2 = Column(String(50), nullable=True)
    lr_num = Column(String(25), nullable=True)
    all_inputs = Column(Text, nullable=False)
    extra_inputs = Column(Text, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    acknowledge = Column(SmallInteger, nullable=True, server_default='0')

class ShipmentLineItems(Base):
    __tablename__ = 'shipment_line_items'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    order_id = Column(Integer, nullable=True)
    product_id = Column(Integer, nullable=True)
    channel_line_item_id = Column(String(50), nullable=True)
    channel_variant_id = Column(String(50), nullable=True)
    product_name = Column(String(200), nullable=False)
    quantity = Column(Integer, nullable=True, server_default='1')
    status = Column(String(50), nullable=True)
    weight = Column(Numeric(20,  2), nullable=False, server_default='0.50')
    weight_unit = Column(String(10), nullable=False)
    weight_in_kgs = Column(Numeric(5,  2), nullable=False)
    product_value = Column(Numeric(20,  2), nullable=False)
    discounted_product_value = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    cancelled_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)

class ShipmentMilestoneDates(Base):
    __tablename__ = 'shipment_milestone_dates'

    shipment_no = Column(BigInteger, nullable=True)
    tracking_id = Column(String(100), nullable=True)
    rto_tracking_id = Column(String(100), nullable=True)
    booking_date = Column(DateTime, nullable=True)
    pickup_requested_date = Column(DateTime, nullable=True)
    pickup_date = Column(DateTime, nullable=True)
    pickup_cancellation_date = Column(DateTime, nullable=True)
    dispatch_date = Column(DateTime, nullable=True)
    estimated_delivery_date = Column(DateTime, nullable=True)
    rto_estimated_delivery_date = Column(DateTime, nullable=True)
    delivered_date = Column(DateTime, nullable=True)
    rto_initiated_date = Column(DateTime, nullable=True)
    rto_delivered_date = Column(DateTime, nullable=True)
    shipment_closed_date = Column(DateTime, nullable=True)
    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    partner_last_update = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class ShipmentOnlinePayments(Base):
    __tablename__ = 'shipment_online_payments'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    vama_transaction_id = Column(BigInteger, nullable=False)
    transaction_id = Column(String(255), nullable=False)
    gateway_name = Column(String(255), nullable=False)
    shipment_amount = Column(Numeric(20,  2), nullable=False)
    transaction_amount = Column(Numeric(20,  2), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class ShipmentOtherDetails(Base):
    __tablename__ = 'shipment_other_details'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    pod_link = Column(String(256), nullable=True)
    otp_verified_delivery = Column(SmallInteger, nullable=True, server_default='0')
    otp_verified_refusal = Column(SmallInteger, nullable=False, server_default='0')
    type_of_otp = Column(String(100), nullable=True)
    signature = Column(Text, nullable=True)
    data = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=True, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=True, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)

class ShipmentPackages(Base):
    __tablename__ = 'shipment_packages'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    shipment_input_id = Column(Integer, nullable=False)
    package_count = Column(Integer, nullable=False, server_default='1')
    length = Column(Numeric(20,  2), nullable=False)
    width = Column(Numeric(20,  2), nullable=False)
    height = Column(Numeric(20,  2), nullable=False)
    unit = Column(String(10), nullable=True)
    weight = Column(Numeric(20,  2), nullable=False)
    weight_unit = Column(String(10), nullable=True)
    volumetric_weight = Column(Numeric(20,  2), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)
    unique_package_id = Column(BigInteger, nullable=True)

class ShipmentPaymentMapping(Base):
    __tablename__ = 'shipment_payment_mapping'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    payment_history_id = Column(Integer, nullable=False)
    shipment_no = Column(BigInteger, nullable=True)
    transaction_unique_id = Column(String(255), nullable=True)
    remark = Column(String(255), nullable=True)
    amount = Column(Numeric(10,  2), nullable=False, server_default='0.00')
    created_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    updated_at = Column(Time, nullable=True)
    deleted_at = Column(Time, nullable=True)

class ShipmentProductDetails(Base):
    __tablename__ = 'shipment_product_details'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    line_item_id = Column(BigInteger, nullable=False)
    property_name = Column(Text, nullable=False)
    property_value = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)

class ShipmentReports(Base):
    __tablename__ = 'shipment_reports'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=False)
    shipment_no = Column(BigInteger, nullable=False)
    tracking_id = Column(String(30), nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    supplier_name = Column(String(100), nullable=False)
    product_solution = Column(String(100), nullable=True)
    product_name = Column(String(200), nullable=True)
    product_value = Column(Numeric(20,  2), nullable=True)
    shipment_zone = Column(String(10), nullable=True)
    shipment_type = Column(String(20), nullable=True)
    shipment_status = Column(String(100), nullable=True)
    status_message = Column(String(100), nullable=True)
    partner_comment = Column(String(200), nullable=True)
    last_update_time = Column(DateTime, nullable=True)
    vamaship_tracking_status = Column(String(100), nullable=True)
    pickup_date = Column(DateTime, nullable=True)
    delivered_date = Column(DateTime, nullable=True)
    rto_initiated_date = Column(DateTime, nullable=True)
    rto_delivered_date = Column(DateTime, nullable=True)
    out_for_delivery_count = Column(Integer, nullable=False, server_default='0')
    ndr_partner_comment = Column(String(200), nullable=True)
    shipper_name = Column(String(100), nullable=True)
    shipper_email = Column(String(100), nullable=True)
    shipper_contact = Column(String(20), nullable=True)
    shipper_address_line_1 = Column(String(200), nullable=True)
    shipper_city = Column(String(100), nullable=True)
    shipper_pincode = Column(String(20), nullable=True)
    consignee_name = Column(String(100), nullable=True)
    consignee_email = Column(String(100), nullable=True)
    consignee_contact = Column(String(20), nullable=True)
    consignee_address_line_1 = Column(String(200), nullable=True)
    consignee_city = Column(String(100), nullable=True)
    consignee_pincode = Column(String(10), nullable=True)
    total_price = Column(Numeric(20,  2), nullable=True)
    weight_in_kgs = Column(Numeric(10,  2), nullable=True)
    package_length = Column(Numeric(10,  2), nullable=True)
    package_width = Column(Numeric(10,  2), nullable=True)
    package_height = Column(Numeric(10,  2), nullable=True)
    shipment_ref1 = Column(String(100), nullable=True)
    shipment_ref2 = Column(String(100), nullable=True)
    shipment_cod_value = Column(Numeric(20,  2), nullable=True)
    quantity = Column(Integer, nullable=True)
    picked_up = Column(Integer, nullable=True)

class ShipmentSettings(Base):
    __tablename__ = 'shipment_settings'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    setting_key = Column(String(30), nullable=True)
    setting_value = Column(String(255), nullable=True)

class ShipmentSkuImages(Base):
    __tablename__ = 'shipment_sku_images'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    hash = Column(String(70), nullable=True)
    url = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class ShipmentSorterImages(Base):
    __tablename__ = 'shipment_sorter_images'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    link = Column(String(500), nullable=True)
    length = Column(Numeric(5,  2), nullable=True)
    length_unit = Column(String(10), nullable=True)
    width = Column(Numeric(5,  2), nullable=True)
    width_unit = Column(String(10), nullable=True)
    height = Column(Numeric(5,  2), nullable=True)
    height_unit = Column(String(10), nullable=True)
    weight = Column(Numeric(5,  2), nullable=True)
    weight_unit = Column(String(10), nullable=True)
    raw_data = Column(String(250), nullable=True)

class ShipmentSupplierResponses(Base):
    __tablename__ = 'shipment_supplier_responses'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    supplier_data = Column(Text, nullable=True)

class ShipmentTrackingDetails(Base):
    __tablename__ = 'shipment_tracking_details'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    unique_identifier = Column(String(50), nullable=False)
    awb_number = Column(String(255), nullable=True)
    supplier_id = Column(Integer, nullable=False)
    tracking_status = Column(Integer, nullable=True)
    partner_tracking_code = Column(String(255), nullable=True)
    tracking_event_date_time = Column(DateTime, nullable=True)
    location = Column(String(255), nullable=True)
    partner_comment = Column(String(500), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)
    additional_details = Column(Text, nullable=True)
    otp_verified = Column(SmallInteger, nullable=True, server_default='0')

class ShipmentWarehouses(Base):
    __tablename__ = 'shipment_warehouses'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    warehouse_id = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=True, server_default=text("'curdate() ON UPDATE current_timestamp()'"))
    updated_at = Column(DateTime, nullable=True)

class ShipmentWeightHistories(Base):
    __tablename__ = 'shipment_weight_histories'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ecom2_table_id = Column(Integer, nullable=True)
    shipment_no = Column(BigInteger, nullable=False)
    shipment_weight = Column(Numeric(10,  2), nullable=True)
    weight_category = Column(String(255), nullable=False)
    weight_source = Column(String(255), nullable=False)
    added_by = Column(String(255), nullable=False)
    added_by_id = Column(Integer, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    weight_category_id = Column(Integer, nullable=False, server_default='3')
    deleted_at = Column(Time, nullable=True)

class Shipments(Base):
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_user_id = Column(Integer, nullable=False)
    accounts_entity_id = Column(Integer, nullable=False)
    shipment_no = Column(BigInteger, nullable=True)
    email = Column(String(255), nullable=True)
    supplier_id = Column(Integer, nullable=False)
    from_pincode = Column(String(10), nullable=True)
    to_pincode = Column(String(10), nullable=True)
    shipment_date = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    product_code = Column(String(10), nullable=False)
    cod_value = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    pre_gst_total_price = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    total_price = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    pre_gst_total_partner_cost = Column(Numeric(20,  2), nullable=False, server_default='0.00')
    total_partner_cost = Column(Numeric(10,  2), nullable=False, server_default='0.00')
    product = Column(String(255), nullable=True)
    product_value = Column(Numeric(20,  2), nullable=True)
    cancelled_at = Column(DateTime, nullable=True)
    bulk_id = Column(String(20), nullable=True)
    tracking_id = Column(String(100), nullable=True)
    booking_status = Column(SmallInteger, nullable=False, server_default='-1')
    lr_num = Column(String(25), nullable=True)
    rto_tracking_id = Column(String(100), nullable=True)
    tracking_status = Column(Integer, nullable=True)
    is_offline = Column(SmallInteger, nullable=False, server_default='0')
    invoice_weight = Column(Numeric(20,  2), nullable=False)
    billable = Column(String(3), nullable=False)
    partner_bill = Column(SmallInteger, nullable=False)
    ecom2_bulk_reference_number = Column(String(100), nullable=True)
    reference1 = Column(String(50), nullable=True)
    reference2 = Column(String(50), nullable=True)
    branch_id = Column(Integer, nullable=True)
    shipment_input_id = Column(Integer, nullable=False)
    pickup_location_id = Column(Integer, nullable=False)
    consignee_location_id = Column(Integer, nullable=False)
    billing_location_id = Column(Integer, nullable=True)
    return_location_id = Column(Integer, nullable=True)
    channel_id = Column(String(100), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)
    shipment_zone = Column(String(150), nullable=True)
    slab_count = Column(Integer, nullable=True)
    billed_price = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    supplier_cost = Column(Numeric(20,  2), nullable=True)
    calculated = Column(SmallInteger, nullable=False, server_default='1')
    multipartner = Column(SmallInteger, nullable=True, server_default='1')
    ip_address = Column(String(25), nullable=True)
    booking_medium = Column(String(25), nullable=True)
    created_at_ist = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    is_entity_spoc = Column(SmallInteger, nullable=False, server_default='0')
    is_stressed = Column(SmallInteger, nullable=False, server_default='0')

class ShopifyFulfillmentLog(Base):
    __tablename__ = 'shopify_fulfillment_log'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(Integer, nullable=False)
    accounts_entity_id = Column(Integer, nullable=True)
    resuest = Column(Text, nullable=True)
    responce = Column(Text, nullable=True)
    error = Column(Text, nullable=True)
    created_at = Column(Time, nullable=True)
    updated_at = Column(Time, nullable=True)
    deleted_at = Column(Time, nullable=True)

class SmartrNdr(Base):
    __tablename__ = 'smartr_ndr'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    awb_no = Column(BigInteger, nullable=True)
    partner_comment = Column(Text, nullable=True)
    tracking_status = Column(String(255), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    ndr_date = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    deleted_at = Column(Time, nullable=True)

class SmartrNdrs(Base):
    __tablename__ = 'smartr_ndrs'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    awb_no = Column(BigInteger, nullable=True)
    partner_comment = Column(Text, nullable=True)
    tracking_status = Column(String(255), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    ndr_date = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    deleted_at = Column(Time, nullable=True)

class SmsLogs(Base):
    __tablename__ = 'sms_logs'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    mobile_no = Column(String(25), nullable=False)
    request_url = Column(String(300), nullable=False)
    request_parameters = Column(Text, nullable=False)
    request_id = Column(String(150), nullable=True)
    response = Column(Text, nullable=False)
    status = Column(String(10), nullable=False)
    delivery_status = Column(String(10), nullable=True)
    comment = Column(String(200), nullable=True)
    delivered_at = Column(DateTime, nullable=True)
    no_of_fragments = Column(SmallInteger, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))

class StagedInvoices(Base):
    __tablename__ = 'staged_invoices'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    accounts_user_id = Column(BigInteger, nullable=True)
    gst_branch_id = Column(BigInteger, nullable=True)
    invoice_no = Column(String(20), nullable=False)
    category_id = Column(Integer, nullable=False)
    against_invoice_no = Column(String(20), nullable=True)
    invoice_type = Column(String(20), nullable=False)
    invoice_temp_no = Column(String(20), nullable=True)
    data = Column(Text, nullable=False)
    total_without_tax = Column(Numeric(20,  2), nullable=False)
    igst = Column(Numeric(20,  2), nullable=False)
    sgst = Column(Numeric(20,  2), nullable=False)
    cgst = Column(Numeric(20,  2), nullable=False)
    tax_total = Column(Numeric(20,  2), nullable=False)
    total = Column(Numeric(20,  2), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)
    file_link = Column(Text, nullable=True)

class StaticAwbNos(Base):
    __tablename__ = 'static_awb_nos'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    awb = Column(String(100), nullable=False)
    order_id = Column(String(20), nullable=True)
    used = Column(SmallInteger, nullable=False, server_default='0')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    user_id = Column(Integer, nullable=False)
    is_cod = Column(SmallInteger, nullable=False)
    is_reverse = Column(SmallInteger, nullable=False, server_default='0')
    deleted_at = Column(Time, nullable=True)

class SupplierApiSettings(Base):
    __tablename__ = 'supplier_api_settings'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(BigInteger, nullable=False)
    soap_api = Column(SmallInteger, nullable=False, server_default='0')
    same_rto_awb = Column(SmallInteger, nullable=False, server_default='0')
    pickup_api = Column(SmallInteger, nullable=False, server_default='1')
    warehouse_api = Column(SmallInteger, nullable=False, server_default='0')
    reverse_awb = Column(SmallInteger, nullable=False, server_default='0')
    custom_label_class = Column(String(200), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class SupplierInvoices(Base):
    __tablename__ = 'supplier_invoices'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    accounts_user_id = Column(BigInteger, nullable=False)
    supplier_id = Column(BigInteger, nullable=False, server_default='0')
    shipment_no = Column(BigInteger, nullable=False)
    invoice_no = Column(String(255), nullable=True)
    supplier_name = Column(String(255), nullable=True)
    awb = Column(String(255), nullable=True)
    return_awn = Column(String(255), nullable=True)
    weight = Column(Numeric(20,  3), nullable=False)
    invoice_amount = Column(Numeric(20,  2), nullable=False)
    details = Column(Text, nullable=True)
    pick_up_date = Column(DateTime, nullable=True)
    invoice_date = Column(DateTime, nullable=True)
    invoice_date_in_excel = Column(DateTime, nullable=True)
    created_by = Column(BigInteger, nullable=True)
    updated_by = Column(BigInteger, nullable=True)
    status = Column(String(255), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    vama_bill = Column(SmallInteger, nullable=False, server_default='0')
    vama_cost = Column(Numeric(20,  2), nullable=True)
    supplier_cost = Column(Numeric(20,  2), nullable=True)
    rto_cost = Column(Numeric(20,  2), nullable=True)
    rto_pending_cost = Column(Numeric(20,  2), nullable=True)
    master_user_id = Column(Integer, nullable=True)
    remark = Column(String(200), nullable=True)
    deleted_at = Column(Time, nullable=True)
    ecom2_table_id = Column(BigInteger, nullable=True)
    invoice_month = Column(String(20), nullable=True)

class SupplierPreferences(Base):
    __tablename__ = 'supplier_preferences'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=True)
    accounts_user_id = Column(Integer, nullable=True)
    supplier_id = Column(Integer, nullable=True)
    type = Column(String(255), nullable=False)
    vas = Column(String(255), nullable=False)
    priority = Column(SmallInteger, nullable=False, server_default='1')
    added_by = Column(Integer, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class SupplierTrackingUrls(Base):
    __tablename__ = 'supplier_tracking_urls'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(BigInteger, nullable=False)
    supplier_tracking_url = Column(Text, nullable=False)

class Suppliers(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(100), nullable=False)
    supplier_api_file = Column(String(100), nullable=True)
    partner_group_id = Column(Integer, nullable=True)
    email = Column(String(100), nullable=False)
    password = Column(String(60), nullable=False)
    is_active = Column(SmallInteger, nullable=False, server_default='1')
    service_type = Column(String(50), nullable=True)
    vamaship_product_code = Column(String(5), nullable=True)
    pricing_class = Column(String(200), nullable=True)
    costing_class = Column(String(250), nullable=True)
    ip_address = Column(String(20), nullable=False)
    pickup_time = Column(String(50), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)
    logo = Column(String(255), nullable=True)
    alias = Column(String(30), nullable=True)
    partner_short_name = Column(String(60), nullable=True)

class SurfaceB2bBuyprice(Base):
    __tablename__ = 'surface_b2b_buyprice'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    route = Column(String(20), nullable=False)
    rate = Column(Float, nullable=False)
    duration = Column(SmallInteger, nullable=True)
    from_date = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(Time, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class SurfaceB2bBuypriceSettings(Base):
    __tablename__ = 'surface_b2b_buyprice_settings'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    setting = Column(String(30), nullable=False)
    from_date = Column(DateTime, nullable=False)
    config = Column(String(255), nullable=True)
    extra = Column(String(200), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class SurfaceB2bChargeMaster(Base):
    __tablename__ = 'surface_b2b_charge_master'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    charge_head = Column(String(30), nullable=False)
    mandatory = Column(SmallInteger, nullable=True, server_default='0')
    description = Column(String(255), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class SurfaceB2bEntitySettings(Base):
    __tablename__ = 'surface_b2b_entity_settings'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    accounts_entity_id = Column(Integer, nullable=True)
    setting = Column(String(30), nullable=False)
    from_date = Column(DateTime, nullable=False)
    config = Column(String(255), nullable=True)
    extra = Column(String(200), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class SurfaceB2bPincodes(Base):
    __tablename__ = 'surface_b2b_pincodes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=False, server_default='0')
    has_cod = Column(SmallInteger, nullable=False, server_default='0')
    has_express = Column(SmallInteger, nullable=False, server_default='0')
    has_cash = Column(SmallInteger, nullable=False, server_default='0')
    has_repl = Column(SmallInteger, nullable=False, server_default='0')
    is_oda = Column(SmallInteger, nullable=True, server_default='0')
    zone = Column(String(10), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    disabled_on = Column(Time, nullable=True)
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    region = Column(String(100), nullable=False)
    is_stressed = Column(SmallInteger, nullable=False, server_default='0')

class SurfaceB2bRates(Base):
    __tablename__ = 'surface_b2b_rates'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    accounts_entity_id = Column(Integer, nullable=True)
    route = Column(String(20), nullable=False)
    rate = Column(Float, nullable=False)
    duration = Column(SmallInteger, nullable=True)
    from_date = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(Time, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class SurfaceB2cCosting(Base):
    __tablename__ = 'surface_b2c_costing'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=True)
    supplier_id = Column(Integer, nullable=False)
    costing_logic = Column(String(255), nullable=False)
    per_slab_cost = Column(Text, nullable=False)
    fuel_surcharge = Column(Float, nullable=False)
    cod_tax = Column(String(100), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    from_date = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    classes = Column(Text, nullable=False)
    extra_charges = Column(Text, nullable=False)
    volumetric_formula = Column(String(255), nullable=False)
    is_reverse = Column(SmallInteger, nullable=False, server_default='0')
    is_rto = Column(SmallInteger, nullable=False, server_default='0')

class SurfaceB2cPincodes(Base):
    __tablename__ = 'surface_b2c_pincodes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=False, server_default='0')
    durations = Column(Text, nullable=False)
    has_cod = Column(SmallInteger, nullable=False)
    has_express = Column(SmallInteger, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    has_cash = Column(SmallInteger, nullable=False)
    has_repl = Column(SmallInteger, nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    region = Column(String(100), nullable=False)
    from_date = Column(DateTime, nullable=True)
    is_stressed = Column(SmallInteger, nullable=False, server_default='0')

class SurfacePincodes(Base):
    __tablename__ = 'surface_pincodes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=False)
    has_express = Column(SmallInteger, nullable=False)
    has_cod = Column(SmallInteger, nullable=False)
    zone = Column(String(10), nullable=False)
    newage = Column(SmallInteger, nullable=False, server_default='0')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class SurfaceRouteToSlab(Base):
    __tablename__ = 'surface_route_to_slab'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    accounts_entity_id = Column(Integer, nullable=True)
    slabs = Column(Text, nullable=False)
    extra_charges = Column(Text, nullable=False)
    from_date = Column(DateTime, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    surface_category = Column(String(10), nullable=False)

class SurfaceZoneToRoute(Base):
    __tablename__ = 'surface_zone_to_route'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    zone_map = Column(String(20), nullable=False)
    route = Column(String(10), nullable=False)
    newage = Column(SmallInteger, nullable=False, server_default='0')
    duration = Column(SmallInteger, nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class TableComments(Base):
    __tablename__ = 'table_comments'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    table_identifier = Column(BigInteger, nullable=False)
    table_name = Column(String(100), nullable=False)
    created_by_table = Column(String(100), nullable=False)
    created_by_id = Column(BigInteger, nullable=False)
    comment = Column(Text, nullable=False)
    attachments = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)

class TemporaryWeightUpload(Base):
    __tablename__ = 'temporary_weight_upload'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    weight = Column(BigInteger, nullable=True)
    e_way_bill = Column(String(50), nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class TrackableShipments(Base):
    __tablename__ = 'trackable_shipments'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    tracking_id = Column(String(20), nullable=False)
    supplier_id = Column(Integer, nullable=False)
    tracking_status = Column(Integer, nullable=False)
    tracking_type = Column(String(20), nullable=True)
    closed_at = Column(Time, nullable=True)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    partner_last_update = Column(DateTime, nullable=True)
    remark = Column(String(255), nullable=True)

class TrackingDashboardLogs(Base):
    __tablename__ = 'tracking_dashboard_logs'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    partner_id = Column(BigInteger, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    successful_count = Column(BigInteger, nullable=False, server_default='0')
    failed_count = Column(BigInteger, nullable=False, server_default='0')
    total_count = Column(BigInteger, nullable=False, server_default='0')
    log_date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    vama_transaction_id = Column(BigInteger, nullable=False)
    sac = Column(BigInteger, nullable=True)
    voucher_no = Column(String(30), nullable=True)
    accounts_entity_id = Column(Integer, nullable=True)
    accounts_user_id = Column(Integer, nullable=True)
    payment_mode = Column(String(100), nullable=True)
    payment_type = Column(String(20), nullable=True)
    accounting_type_id = Column(Integer, nullable=False)
    transaction_amount = Column(Numeric(20,  2), nullable=False)
    transaction_unique_id = Column(String(100), nullable=True)
    transaction_by = Column(BigInteger, nullable=False)
    remark = Column(Text, nullable=True)
    invoice_no = Column(String(50), nullable=True)
    quick_books_id = Column(String(20), nullable=True)
    qb_transaction_id = Column(String(50), nullable=True)
    qb_payment_id = Column(String(50), nullable=True)
    status = Column(SmallInteger, nullable=False, server_default='0')
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    deleted_at = Column(DateTime, nullable=True)
    gateway_name = Column(String(255), nullable=True)
    payment_request_token = Column(String(255), nullable=True)
    payment_status = Column(String(255), nullable=True)
    reference_table = Column(String(255), nullable=True)
    reference_id = Column(String(255), nullable=True)
    received_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    credit_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    debit_amount = Column(Numeric(20,  2), nullable=True, server_default='0.00')
    transaction_status = Column(SmallInteger, nullable=True, server_default='0')
    zohobook_id = Column(String(30), nullable=True)

class UnusedInvoiceNumbers(Base):
    __tablename__ = 'unused_invoice_numbers'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    invoice_no = Column(String(30), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class UploadHistory(Base):
    __tablename__ = 'upload_history'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=False)
    accounts_user_id = Column(Integer, nullable=False)
    feature = Column(String(50), nullable=False)
    data = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class UpsellProducts(Base):
    __tablename__ = 'upsell_products'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=True)
    product_info = Column(Text, nullable=False)
    is_active = Column(SmallInteger, nullable=True, server_default='1')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class UserNotificationHistory(Base):
    __tablename__ = 'user_notification_history'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=False)
    notification_id = Column(Integer, nullable=False)
    closed_at = Column(Time, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))

class UserNotificationsSettings(Base):
    __tablename__ = 'user_notifications_settings'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_user_id = Column(BigInteger, nullable=True)
    type = Column(String(30), nullable=False)
    event = Column(String(200), nullable=False)
    notifications_content = Column(Text, nullable=True)
    recipient = Column(String(20), nullable=False)
    active = Column(SmallInteger, nullable=True, server_default='1')
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

class UserPartnerPreferences(Base):
    __tablename__ = 'user_partner_preferences'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_rules_table_id = Column(Integer, nullable=True)
    ecom2_user_id = Column(Integer, nullable=False)
    accounts_user_id = Column(Integer, nullable=False)
    accounts_entity_id = Column(Integer, nullable=False)
    transport_type = Column(String(255), nullable=False)
    service_type = Column(String(255), nullable=False)
    product_category = Column(String(255), nullable=False)
    deactivated_on = Column(Time, nullable=True)
    is_cheapest_first_preference_enabled = Column(SmallInteger, nullable=False, server_default='0')
    is_custom_preference_enabled = Column(SmallInteger, nullable=False, server_default='1')
    vas = Column(String(255), nullable=True)
    available_suppliers = Column(String(255), nullable=True)
    custom_partner_preference = Column(String(255), nullable=True)
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    created_at = Column(Time, nullable=False)
    updated_at = Column(Time, nullable=False)
    deleted_at = Column(Time, nullable=True)

class UserRules(Base):
    __tablename__ = 'user_rules'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(Integer, nullable=True)
    type = Column(String(255), nullable=True)
    rule = Column(Text, nullable=False)
    active = Column(SmallInteger, nullable=False, server_default='1')
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    accounts_user_id = Column(BigInteger, nullable=True)
    api_key = Column(String(80), nullable=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(150), nullable=False)
    country_code = Column(String(10), nullable=False)
    mobile = Column(String(20), nullable=True)
    is_active = Column(Integer, nullable=True, server_default='1')
    send_emails = Column(SmallInteger, nullable=True, server_default='1')
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(DateTime, nullable=True)

class ValuableAirCosting(Base):
    __tablename__ = 'valuable_air_costing'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    costing_logic = Column(String(255), nullable=False)
    per_slab_cost = Column(Text, nullable=False)
    service_tax = Column(Float, nullable=True)
    fuel_surcharge = Column(Float, nullable=False)
    cod_tax = Column(String(100), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    from_date = Column(Time, nullable=True, server_default=text('current_timestamp()'))
    classes = Column(Text, nullable=False)
    extra_charges = Column(Text, nullable=False)
    volumetric_formula = Column(String(255), nullable=False)
    accounts_entity_id = Column(Integer, nullable=True)
    is_reverse = Column(SmallInteger, nullable=False, server_default='0')
    is_rto = Column(SmallInteger, nullable=False, server_default='0')

class ValuableAirPincodes(Base):
    __tablename__ = 'valuable_air_pincodes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_id = Column(Integer, nullable=False)
    pincode = Column(Integer, nullable=False)
    is_origin = Column(SmallInteger, nullable=False, server_default='0')
    durations = Column(Text, nullable=False)
    has_cod = Column(SmallInteger, nullable=False)
    has_express = Column(SmallInteger, nullable=False)
    has_cash = Column(SmallInteger, nullable=False)
    has_repl = Column(SmallInteger, nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    region = Column(String(100), nullable=False)
    created_at = Column(Time, nullable=False, server_default=text('current_timestamp()'))
    updated_at = Column(Time, nullable=True, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    from_date = Column(DateTime, nullable=True)

class VamashipTrackingCodesMaster(Base):
    __tablename__ = 'vamaship_tracking_codes_master'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    old_code = Column(String(10), nullable=True)
    new_code = Column(Integer, nullable=True)
    tracking_category = Column(String(50), nullable=True)
    status_message = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

class Vendors(Base):
    __tablename__ = 'vendors'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    accounts_entity_id = Column(BigInteger, nullable=False)
    user_id = Column(BigInteger, nullable=True)
    vendor_name = Column(String(300), nullable=True)
    vendor_reference_id = Column(String(100), nullable=True)
    email = Column(String(255), nullable=False)

class WeightCategories(Base):
    __tablename__ = 'weight_categories'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    category_code = Column(String(10), nullable=True)

class WeightDisputes(Base):
    __tablename__ = 'weight_disputes'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=False)
    accounts_entity_id = Column(BigInteger, nullable=False)
    status = Column(SmallInteger, nullable=True, server_default='0')
    booked_weight = Column(Numeric(20,  3), nullable=False)
    invoice_weight = Column(Numeric(20,  3), nullable=False)
    settled_weight = Column(Numeric(20,  3), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    raised_by = Column(Integer, nullable=True)
    raised_from = Column(String(20), nullable=True)
    updated_by = Column(String(100), nullable=True)
    updated_at = Column(DateTime, nullable=False, server_default=text("'current_timestamp() ON UPDATE current_timestamp()'"))
    deleted_at = Column(Time, nullable=True)
    settled_at = Column(Time, nullable=True)
    dispute_proofs = Column(Text, nullable=True)
    partner_proofs = Column(Text, nullable=True)
    shipper_remark = Column(Text, nullable=True)
    supplier_remark = Column(Text, nullable=True)
    invoiced_by_partner = Column(SmallInteger, nullable=True, server_default='0')

class WhatsappLogs(Base):
    __tablename__ = 'whatsapp_logs'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    api_user_id = Column(String(15), nullable=False)
    message_id = Column(String(100), nullable=True)
    customer_phone = Column(String(15), nullable=False)
    shipment_no = Column(BigInteger, nullable=True)
    event_type = Column(String(30), nullable=False)
    message = Column(Text, nullable=False)
    whatsapp_account_number = Column(String(15), nullable=True)
    replied_on = Column(DateTime, nullable=True)
    customer_name = Column(String(100), nullable=True)
    reply_text = Column(String(100), nullable=True)
    response = Column(Text, nullable=False)
    status = Column(String(20), nullable=True)
    created_at = Column(DateTime, nullable=True, server_default=text('current_timestamp()'))

class WhatsappLogsOrderVerification(Base):
    __tablename__ = 'whatsapp_logs_order_verification'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    order_no = Column(BigInteger, nullable=True)
    api_user_id = Column(String(15), nullable=False)
    message_id = Column(String(100), nullable=True)
    event_type = Column(String(60), nullable=False)
    customer_phone = Column(String(15), nullable=False)
    message = Column(Text, nullable=False)
    whatsapp_account_number = Column(String(15), nullable=True)
    replied_on = Column(DateTime, nullable=True)
    customer_name = Column(String(100), nullable=True)
    reply_text = Column(String(100), nullable=True)
    response = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=True, server_default=text('current_timestamp()'))

class WoocommerceFulfillmentLog(Base):
    __tablename__ = 'woocommerce_fulfillment_log'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(String(255), nullable=False)
    accounts_entity_id = Column(Integer, nullable=False)
    request = Column(Text, nullable=True)
    response = Column(Text, nullable=True)
    error = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=text('current_timestamp()'))

class XbTrackingCallbackDetails(Base):
    __tablename__ = 'xb_tracking_callback_details'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    shipment_no = Column(BigInteger, nullable=True)
    request_details = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

# Dynamic table reflection - allows querying any table without defining a model
metadata = MetaData()

def get_table(table_name):
    """Get a table object by name (for dynamic queries)"""
    if table_name not in metadata.tables:
        Table(table_name, metadata, autoload_with=engine)
    return metadata.tables[table_name]

def get_all_tables():
    """Get all table names from the database"""
    inspector = inspect(engine)
    return inspector.get_table_names()
